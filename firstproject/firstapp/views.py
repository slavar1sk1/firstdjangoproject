from django.shortcuts import render
from .models import User, Post
from .forms import PostCreateForm, RegistrationForm, LoginForm
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

__all__ = ('HomeView', 'PostCreateView', 'RegistrationView', 'UserLoginView')


# Create your views here.
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'


class PostCreateView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = "posts.html"
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class RegistrationView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = "registration.html"
    success_url = "/"


class UserLoginView(LoginView):
    model = User
    template_name = "login.html"
    form_class = LoginForm
    redirect_authenticated_user = True
