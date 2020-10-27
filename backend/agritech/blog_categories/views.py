from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.db.models import Q

from .models import BlogCategory
from blogs.serializers import BlogCategorySerializer

from rest_framework.decorators import api_view

#Django GET request to retrieve all blog categories stored in the database as a JSON response
@api_view(['GET'])
def category(request, slug):
    if request.method == 'GET':
        try:
            #retrieve all blog categories ordered by the created date
            categories = BlogCategory.objects.filter(slug=slug)
            categories_serializer = BlogCategorySerializer(categories, many=True)

            response = {
                'message': "Get all Blog Categories Successfully",
                'blogs': categories_serializer.data,
                'error': ""
            }
            return JsonResponse(response, status=status.HTTP_200_OK);
        except:
            error = {
                'message': "Fail! -> can NOT get all Blog Categories List. Please check again!",
                'blogs': "[]",
                'error': "Error"
            }
        return JsonResponse(error, status=status.HTTP_404_NOT_FOUND)