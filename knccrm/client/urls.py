from django.urls import path

from . import views

urlpatterns = [
    path('', views.client_list, name='client_list'),
    path('add/' , views.add_client, name='add_client'),
    path('<int:pk>/', views.client_details, name='client_details'),
    path('<int:pk>/delete/', views.delete_client, name='delete_client'),
    path('<int:pk>/edit/', views.client_edit , name='client_edit'),
    path('update/bulk/', views.update_priority_client_bulk, name='update_priority_client_bulk'),
]