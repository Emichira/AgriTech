from django.urls import path
from users.views import SellerRegistrationView, BuyerRegistrationView, RegistrationPageView

app_name = 'users'

urlpatterns = [
    #registration page url to ask the user if they want to sign up as a seller or as a buyer
    path('registration/', RegistrationPageView.as_view(), name='signup'),
    #url to handle sign up authentication as a seller
    path('registration/seller/', SellerRegistrationView.as_view(), name='register_seller'),
    #url to handle sign up authentication as a buyer
    path('registration/buyer/', BuyerRegistrationView.as_view(), name='register_buyer'),
]