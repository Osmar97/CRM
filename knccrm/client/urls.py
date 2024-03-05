from django.urls import path

from . import views

urlpatterns = [
    path('', views.client_list, name='client_list'),
    path('add/' , views.add_client, name='add_client'),
    path('update/bulk/', views.update_priority_client_bulk, name='update_priority_client_bulk'),
]