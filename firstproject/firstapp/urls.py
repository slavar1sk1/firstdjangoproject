from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('post_detail/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/comment/', PostCommentView.as_view(), name='add_comment'),
    path('comment/<int:id>/delete', DeleteCommentView.as_view(), name='delete_comment'),
    path('like_post/<int:post_id>/', LikePostView.as_view(), name='like_post'),
    path('post_create/', PostCreateView.as_view(), name='create_post'),
    path('like_home/<int:post_id>/', HomeLikeView.as_view(), name='like_home'),
    path('profil/', ProfilView.as_view(), name='profil'),


]