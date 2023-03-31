from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('result/', views.result, name='result'),
    path('dados/', views.dadosGrafico, name='dadosGrafico'),
    path('processament/', views.processament, name='processament'),
    path('get_processing_status/', views.get_processing_status, name='get_processing_status'),
    path('get_uploaded_file/', views.get_uploaded_file, name='get_uploaded_file'),
    path('download/<str:project>/', views.download_folder, name='download_folder'),
]
