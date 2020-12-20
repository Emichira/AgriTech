from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Seller, Buyer

class UserAdmin(UserAdmin):
    list_display = ['email', 'is_buyer', 'is_seller']
    list_display_links = ('email', 'is_buyer', 'is_seller')
    list_filter = ('is_buyer', 'is_seller')
    search_fields = ('email',)
    list_per_page = 50

admin.site.register(User, UserAdmin)
admin.site.register(Seller)
admin.site.register(Buyer)