
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('masomoapp.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # Default authentication URLs
]
