from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("clonepen.com/admin/", admin.site.urls),
    path('clonepen.com/', include('accounts.urls')),
    path('clonepen.com/', include('core.urls')),
    path('clonepen.com/api/', include('api.urls')),
]
