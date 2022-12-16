from django.views.generic import CreateView
from .forms import RegisterForm, CustomUserCreationForm
from .models import CustomUser
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.contrib import messages



# Create your views here.

# function based view
def register(request):
    template = 'registration/registration.html'
    if request.method == 'GET':
        form = RegisterForm
        context = {
            'form': form,
        }
        return render(request, template, context)
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('email')
            success_message = f'Account for {user} has been created successfully.'
            messages.success(request, success_message)
            return redirect('login')
        else:
            print("INVALID FORM")
            messages.error(request, 'Error Processing Your Request')
            context = {
                'form': form
            }
            return render(request, template, context)

    return render(request, template, {})

# class based register view
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

