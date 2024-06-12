from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('post_detail/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/comment/', PostCommentView.as_view(), name='add_comment'),
]