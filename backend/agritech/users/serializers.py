from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework.authtoken.models import Token

from .models import Seller, Buyer

# A user serializer for registering a seller
class SellerCustomRegistrationSerializer(RegisterSerializer):
    seller = serializers.PrimaryKeyRelatedField(read_only=True,) #by default allow_null = False
    phone_number = serializers.CharField(required=True)
    county = serializers.CharField(required=True)
    country = serializers.CharField(required=True)
    description = serializers.CharField(required=True)

    def get_cleaned_data(self):
            data = super(SellerCustomRegistrationSerializer, self).get_cleaned_data()
            extra_data = {
                'phone_number' : self.validated_data.get('phone_number', ''),
                'county' : self.validated_data.get('county', ''),
                'country ' : self.validated_data.get('country ', ''),
                'description': self.validated_data.get('description', ''),
            }
            data.update(extra_data)
            return data

    def save(self, request):
        user = super(SellerCustomRegistrationSerializer, self).save(request)
        user.is_seller = True
        user.save()
        seller = Seller(seller=user, phone_number=self.cleaned_data.get('phone_number'),
                county=self.cleaned_data.get('county'),
                country=self.cleaned_data.get('country'),
                description=self.cleaned_data.get('description'))
        seller.save()
        return user

# A user serializer for registering a buyer
class BuyerCustomRegistrationSerializer(RegisterSerializer):
    buyer = serializers.PrimaryKeyRelatedField(read_only=True,) #by default allow_null = False

    def get_cleaned_data(self):
            data = super(BuyerCustomRegistrationSerializer, self).get_cleaned_data()
            return data

    def save(self, request):
        user = super(BuyerCustomRegistrationSerializer, self).save(request)
        user.is_buyer = True
        user.save()
        buyer = Buyer(buyer=user)
        buyer.save()
        return user