from django import forms
from .models import Post, User, Comment
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# class Post(forms.Form):
#     text = forms.CharField(widget=forms.Textarea(attrs={"class": "text",
#                                                       "placeholder": "Some text here"}), label='', max_length=3000)


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget = forms.Textarea(attrs={"class": "text", "placeholder": "Some text here"})


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']



