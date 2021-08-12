from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('users', include('users.urls')),
    path('products', include('products.urls')),
    path('orders', include('orders.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)