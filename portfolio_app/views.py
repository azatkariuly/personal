from django.shortcuts import render
from django.http import HttpResponse
from portfolio_app.models import News, Comment

from django.views.generic import (ListView, DetailView)

# Create your views here.

def about(request):
    return render(request, 'portfolio_app/about.html')

def news(request):
    return render(request, 'portfolio_app/news.html')

def projects(request):
    return render(request, 'portfolio_app/projects.html')

def publications(request):
    return render(request, 'portfolio_app/publications.html')

def index(request):
    return render(request, 'portfolio_app/index.html')

class NewsListView(ListView):
    context_object_name = 'news_list'
    model = News
    template_name = 'portfolio_app/news/news_list.html'

    def get_queryset(self):
        return News.objects.order_by('-create_date')

class NewsDetailView(DetailView):
    model = News
    template_name = 'portfolio_app/news/news_detail.html'

