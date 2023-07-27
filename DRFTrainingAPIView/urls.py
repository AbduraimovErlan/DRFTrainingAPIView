from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('APIView.urls')),
    path('api/v1/', include('APIView2.urls')),
    path('api/v1/', include('APIView3.urls')),
    path('api/v1/', include('APIView4.urls')),
    path('api/v1/', include('APIView5.urls')),
    path('api/v1/', include('APIView6.urls')),
]
