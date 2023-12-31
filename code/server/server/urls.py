from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('gateway.urls')),
    path('api/profile/', include('user_profile.urls')),
    path('api/norm/', include('normalization.urls')),
    path('api/imputation/', include('imputation.urls')),
    path('api/one_hot_encoding/', include('one_hot_encoding.urls')),
    path('api/file/', include('file_controller.urls')),
]
