from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from .models import Post, Comment
from django.urls import reverse_lazy
from django.views import View

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

class AdsListView(ListView):
    queryset = Post.objects.all()
    template_name = 'ads/ads_list.html'
    # model = Post
    context_object_name = 'ads'

class AdsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'ads/ads_edit.html'
    model = Post
    context_object_name = 'ad'
    fields = ['title', 'region', 'town', 'address', 'body', 'category', 'rental_rate', 'photo_1', 'photo_2', 'photo_3', 'photo_4']

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class AdsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'ads/ads_delete.html'
    model = Post
    success_url = reverse_lazy('ads_list')
    context_object_name = 'ad'
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    
# class AdsDetailView(DetailView):
#     model = Post
#     template_name = 'ads/ads_detail.html'
#     context_object_name = 'ad'

class AdsDetailView(View):
    def get(self, request, *args, **kwargs):
        model = Post
        template = 'ads/ads_detail.html'
        ad = get_object_or_404(model, pk=kwargs['pk'])
        context = {
            'ad': ad,
        }
        return render(request, template, context)
    
    def post(self, request, *args, **kwargs):
        author = self.request.user
        data = self.request.POST
        blog = get_object_or_404(Post, pk=kwargs['pk'])
        comment = data['comment']

        c = Comment(author=author, ad=blog, comment=comment)
        c.save()

        model = Post
        template = 'ads/ads_detail.html'
        ad = get_object_or_404(model, pk=kwargs['pk'])
        context = {
            'ad': ad,
        }
        
        return render(request, template, context)


class AdsCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'ads/ads_create.html'
    fields = ['title', 'address', 'town', 'region', 'category', 'body', 'rental_rate', 'photo_1', 'photo_2', 'photo_3', 'photo_4']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostComment(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'ads/ads_detail.html'
    fields = ['comment']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.ad = self.request.pk
        return super().form_valid(form)

class CategoryFilterView(View):
    def get(self, request, *args, **kwargs):
        model = Post
        template = 'ads/ads_list.html'
        data = self.request.GET
        ads = []
        
        if 'q' in data.keys():
            ads = ads + list(model.objects.filter(body__contains=data['q']))
            ads = ads + list(model.objects.filter(title__contains=data['q']))
            ads = ads + list(model.objects.filter(address__contains=data['q']))
            ads = ads + list(model.objects.filter(region__contains=data['q']))
        else:
            ads = list(model.objects.all())
        
        if 'cat' in data.keys():
            category = data['cat']
            ads_c = list(model.objects.filter(category__contains=category))
            final_ads = []
            for ad in ads:
                if ad in ads_c:
                    final_ads.append(ad)
        else:
            final_ads = ads

        if 'min_price' in data.keys() or 'max_price' in data.keys():
            if  'min_price' in data.keys():
                min_price = int(data['min_price'])
            else:
                min_price = 0
                
            if  'max_price' in data.keys():
                max_price = int(data['max_price'])
            else:
                max_price = 99999999999999

            price_filter = []
            for ad in final_ads:
                if (int(ad.rental_rate) >= min_price) and ( int(ad.rental_rate) <= max_price):
                    price_filter.append(ad)
            final_ads = price_filter

        unique_result = []
        for ad in final_ads:
            if ad not in unique_result:
                unique_result.append(ad)

        context = {
            'ads': unique_result,
        }
        return render(request, template, context)
