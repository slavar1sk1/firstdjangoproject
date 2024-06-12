from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import User, Post, Comment
from .forms import PostCreateForm, RegistrationForm, LoginForm, CommentForm
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.generic.detail import SingleObjectMixin
from django.views.generic import View


__all__ = ('HomeView', 'RegistrationView', 'UserLoginView', 'PostDetailView', 'PostCommentView')


class HomeView(LoginRequiredMixin, ListView):
    template_name = 'index.html'
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user).order_by('-create_at')

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
            html_post = render_to_string(
                'posts_list.html',
                context={
                    'posts': Post.objects.filter(user=self.request.user).order_by('-create_at')
                }
            )

        return JsonResponse(html_post, safe=False)


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=self.object).order_by('-create_at')
        context['comment_form'] = CommentForm()
        return context

class PostCommentView(SingleObjectMixin, View):
    model = Post
    form_class = CommentForm

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.form_class(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = self.object
            comment.save()
            return redirect('post_detail', pk=self.object.pk)

        context = self.get_context_data(object=self.object)
        context['comment_form'] = form
        return self.render_to_response(context)
