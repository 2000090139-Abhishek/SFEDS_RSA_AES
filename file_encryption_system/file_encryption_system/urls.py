from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('file_encrypt/', include('file_encrypt.urls')),
    path('', include('file_encrypt.urls')),
]
