from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import User, Post
from .forms import PostCreateForm, RegistrationForm, LoginForm

__all__ = ('HomeView', 'RegistrationView', 'UserLoginView', 'PostDetailView')


class HomeView(LoginRequiredMixin, ListView):
    template_name = 'index.html'
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Posts'
        context['form'] = PostCreateForm()
        return context

    def post(self, request, *args, **kwargs):
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('/')
        return self.get(request, *args, **kwargs)


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


class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = 'post_detail'
