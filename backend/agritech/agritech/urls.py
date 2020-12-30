from django.urls import path, include
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
# from api.views import BuyerSignUpView, SellerSignUpView
from django.views.generic import TemplateView

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('api/', include('users.urls', namespace='api')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('blogs/categories/', include('blog_categories.urls')),
    path('blogs/', include('blogs.urls')),
    path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
