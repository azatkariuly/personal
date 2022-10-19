from django.urls import path
from simplesocial.posts import views

app_name = 'posts'

urlpatterns = [
    path('', views.PostListClass.as_view(), name='all'),
    path('new/', views.CreatePost.as_view(), name='create'),
    path('by/<username>/', views.UserPosts.as_view(), name='for_user'),
    path('by/<username>/<pk>/', views.PostDetail.as_view(), name='single'),
    path('delelte/<pk>/', views.DeletePost.as_view(), name='delete')
]
