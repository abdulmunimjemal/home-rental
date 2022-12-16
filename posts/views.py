from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from .models import Post, Comment
from django.urls import reverse_lazy, reverse
from django.views import View
from django.http import HttpResponseRedirect

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from environs import Env # some constanrs are there
env = Env()
env.read_env()

# Create your views here.

class AdsListView(ListView):
    queryset = Post.objects.all()
    template_name = 'post/list.html'
    # model = Post
    context_object_name = 'posts'

class FavPostsView(View, LoginRequiredMixin):
    def get(self, request, *args, **kwargs):
        template = 'post/list.html'
        posts = Post.objects.all()
        favorites = []
        for post in posts:
            if post.likes.filter(id=self.request.user.id).exists():
                favorites.append(post)

        context = {
            'posts': favorites,
        }
        return render(request, template, context)
    
class PostLikeAction(View, LoginRequiredMixin):
    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        if post.likes.filter(id=self.request.user.id).exists():
            post.likes.remove(self.request.user)
        else:
            post.likes.add(self.request.user)
        
        return HttpResponseRedirect(reverse('view', args=[str(post.id)]))

    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse('login'))


class OwnPostsView(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request, *args, **kwargs):
        model = Post
        template = 'post/own_list.html'
        posts = model.objects.filter(author=self.request.user)
        if self.request.user.is_superuser:
            posts = model.objects.all()
        context = {
            'posts': posts,
        }
        return render(request, template, context)

    def test_func(self):
        return (self.request.user.user_type == "seller" ) or (True == self.request.user.is_superuser)



class AdsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'post/edit.html'
    model = Post
    context_object_name = 'post'
    fields = ['title', 'region', 'town', 'address', 'body', 'category', 'rental_rate', 'photo_1', 'photo_2', 'photo_3', 'photo_4']

    def test_func(self):
        obj = self.get_object()
        return (obj.author == self.request.user) or (True == self.request.user.is_superuser)

class AdsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'post/delete.html'
    model = Post
    success_url = reverse_lazy('my_posts')
    context_object_name = 'post'
    
    def test_func(self):
        obj = self.get_object()
        return (obj.author == self.request.user) or (True == self.request.user.is_superuser)
    
# class AdsDetailView(DetailView):
#     model = Post
#     template_name = 'ads/ads_detail.html'
#     context_object_name = 'ad'

class AdsDetailView(View):
    def get(self, request, *args, **kwargs):
        model = Post
        template = 'post/view.html'
        post = get_object_or_404(model, pk=kwargs['pk'])
        
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        number_of_likes = post.number_of_likes()
        
        context = {
            'post': post,
            'liked': liked,
            'number_of_likes': number_of_likes
        }
        return render(request, template, context)
    
    def post(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            author = self.request.user
            data = self.request.POST
            blog = get_object_or_404(Post, pk=kwargs['pk'])
            comment = data['comment']
            c = Comment(author=author, ad=blog, comment=comment)
            c.save()
           

            model = Post

            template = 'post/view.html'
            post = get_object_or_404(model, pk=kwargs['pk'])
            liked = False
            if post.likes.filter(id=self.request.user.id).exists():
                liked = True
            number_of_likes = post.number_of_likes()
            
            context = {
                'post': post,
                'liked': liked,
                'number_of_likes': number_of_likes
            }
            return render(request, template, context)
        else:
            return HttpResponseRedirect(reverse('login'))


class AdsCreateView(LoginRequiredMixin, CreateView, UserPassesTestMixin):
    model = Post
    template_name = 'posts/new.html'
    fields = ['title', 'address', 'town', 'region', 'category', 'body', 'rental_rate', 'photo_1', 'photo_2', 'photo_3', 'photo_4']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        obj = self.get_object()
        return ('seller' == self.request.user.user_type) or (True == self.request.user.is_superuser)
    
    
    

class CategoryFilterView(View):
    def get(self, request, *args, **kwargs):
        model = Post
        template = 'post/list.html'
        data = self.request.GET
        ads = []
        
        if 'q' in data.keys():
            ads = ads + list(model.objects.filter(body__contains=data['q']))
            ads = ads + list(model.objects.filter(title__contains=data['q']))
            ads = ads + list(model.objects.filter(address__contains=data['q']))
            ads = ads + list(model.objects.filter(region__contains=data['q']))
        else:
            ads = list(model.objects.all())
        
        if 'cat' in data.keys() and data['cat'] != 'category':
            category = data['cat']
            ads_c = list(model.objects.filter(category__contains=category))
            final_ads = []
            for ad in ads:
                if ad in ads_c:
                    final_ads.append(ad)
        else:
            final_ads = ads

        if 'price' in data.keys():
            min_price = env.int('MIN_PRICE')
            max_price = int(data['price'])

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
            'posts': unique_result,
        }
        return render(request, template, context)
