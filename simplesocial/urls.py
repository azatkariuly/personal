from django.contrib import admin
from django.urls import path, include
from simplesocial import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.HomePage.as_view(), name='simplesocial_home'),
    path('accounts/', include('simplesocial.accounts.urls', namespace='accounts')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('posts/', include('simplesocial.posts.urls', namespace='posts')),
    path('groups/', include('simplesocial.groups.urls', namespace='groups')),
    path('test/', views.TestPage.as_view(), name='test'),
    path('thanks/', views.ThanksPage.as_view(), name='thanks'),
]