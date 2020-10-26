from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.db.models import Q

from .models import Blog
from .serializers import BlogSerializer

from rest_framework.decorators import api_view

#Django GET request to retrieve all blog articles stored in the database as a JSON response
@csrf_exempt
@api_view(['GET'])
def blogs(request):
    if request.method == 'GET':
        try:
            #retrieve all blogs ordered by the blog date
            blogs = Blog.objects.order_by('blog_date')
            blogs_serializer = BlogSerializer(blogs, many=True)

            response = {
                'message': "Get all Blogs Successfully",
                'blogs': blogs_serializer.data,
                'error': ""
            }
            return JsonResponse(response, status=status.HTTP_200_OK);
        except:
            error = {
                'message': "Fail! -> can NOT get all the blogs List. Please check again!",
                'blogs': "[]",
                'error': "Error"
            }
            return JsonResponse(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#Django GET request to retrieve a detailed blog articles stored in the database as a JSON response
@api_view(['GET'])
def blog_detail(request, slug):

    if request.method == 'GET':
        try:
            #retrieve a detailed blog
            blog = Blog.objects.filter(slug=slug)
            blogs_serializer = BlogSerializer(blog, many=True)
            response = {
                'message': "Get a Blog Successfully",
                'blogs': blogs_serializer.data,
                'error': ""
            }
            return JsonResponse(response, status=status.HTTP_200_OK);
        except:
            error = {
                'message': "The blog does not exist",
                'blogs': "[]",
                'error': "Error"
            }
        return JsonResponse(error, status=status.HTTP_404_NOT_FOUND)

#Django GET RestAPI to search all blog articles with a given title in the database as a JSON response
@api_view(['GET'])
def blog_search(request, title):
    try:
        #search blogs queryset based on the title, blog author, country or town
        blogs = Blog.objects.filter(Q(title__icontains=title) | Q(blog_author__icontains=title) |
         Q(country__icontains=title))

        if request.method == 'GET':
            blogs_serializer = BlogSerializer(blogs, many=True)
            response = {
                'message': "Successfully filter all blogs with title = %s" % title,
                'blogs': blogs_serializer.data,
                'error': ""
            }
            # In order to serialize objects, we must set 'safe=False'
            return JsonResponse(response, safe=False)
    except:
        exceptionError = {
                'message': "Fail to get a blog with title = %s" % title ,
                'blogs': "[]",
                'error': "Raise an Exception!"
            }
        return JsonResponse(exceptionError, status=status.HTTP_500_INTERNAL_SERVER_ERROR);

#Django GET request to retrieve a blog articles stored in the database as a JSON response
@api_view(['GET'])
def blog_list_published(request):

    if request.method == 'GET':
        try:
            #retrieve all published blogs
            blogs = Blog.objects.filter(is_published=True)
            blogs_serializer = BlogSerializer(blogs, many=True)
            response = {
                'message': "Get all published Blogs Successfully",
                'blogs': blogs_serializer.data,
                'error': ""
            }
            return JsonResponse(response, status=status.HTTP_200_OK);
        except:
            error = {
                'message': "Fail! can NOT get all the blogs List. Please check again!",
                'blogs': "[]",
                'error': "Error"
            }
            return JsonResponse(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)