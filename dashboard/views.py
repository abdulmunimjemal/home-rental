from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

from django.views.generic import TemplateView, DetailView

class HomePageView(TemplateView):
    template_name = 'home.html'

class ProfileView(TemplateView, LoginRequiredMixin):
    template_name = 'profile/own.html'
