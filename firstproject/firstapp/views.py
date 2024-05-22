from django.shortcuts import render
from .models import User
from .forms import Post
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    return render(request, 'index.html')


def create_post(request):
    if request.method == 'POST':
        form = Post(request.POST)

        if form.is_valid():
            HttpResponseRedirect('/')

    else:
        form = Post()

    return render(request, "posts.html", {'form': form})
