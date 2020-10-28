from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from . import views

urlpatterns = [
    #url to display all blog articles
    path('', views.blogs, name='blogs'),
    #url to display a detailed blog page
    path('<str:slug>/', views.blog_detail, name='blog_detail'),
    #url to display all searched blogs given a blog title, blog author, country or town
    path('search/<str:title>', views.blog_search, name='blog_search'),
    #url to display all published blog articles
    path('published', views.blog_list_published, name='blog_list_published'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)