from django.urls import path
from . import views

app_name = 'file_encrypt'

urlpatterns = [
    path('upload/',views. upload_file, name='upload_file'),
    path('files/', views.file_list, name='file_list'),
    path('files/<int:file_id>/decrypt/', views.decrypt_file_view, name='decrypt_file'),
]
