from django.urls import path
from portfolio_app import views

urlpatterns = [
    path('', views.about, name='about'),
    path('news/', views.NewsListView.as_view(), name='news_list'),
    path('news/<int:pk>/', views.NewsDetailView.as_view(), name='news_detail'),
    path('projects/', views.projects, name='projects'),
    path('publications/', views.publications, name='publications'),
]