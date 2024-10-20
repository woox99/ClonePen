from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('clonepen.com/', include('accounts.urls')),
    path('clonepen.com/', include('core.urls')),
    # path('', include('api.urls')),
]
