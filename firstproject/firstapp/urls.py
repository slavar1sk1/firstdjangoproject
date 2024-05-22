from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('create_post', create_post, name='posts')
]