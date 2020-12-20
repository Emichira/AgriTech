from django.shortcuts import render
from rest_auth.registration.views import RegisterView
from rest_framework.views import APIView
from rest_framework.response import Response

from users.serializers import (
    SellerCustomRegistrationSerializer, BuyerCustomRegistrationSerializer
    )
#Registration page API view to ask user if they want to sign up as a seller or as a buyer
class RegistrationPageView(APIView):
    def get(self, request):
        content = {'message': 'Registration Page'}
        return Response(content)

class SellerRegistrationView(RegisterView):
    serializer_class = SellerCustomRegistrationSerializer

class BuyerRegistrationView(RegisterView):
    serializer_class = BuyerCustomRegistrationSerializer