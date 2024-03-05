from django.urls import path

from . import views

urlpatterns = [
    path('', views.lead, name='lead'),
    path('add-lead/', views.add_lead, name='add_lead'),
    path('show-lead/', views.show_lead, name='show_lead'),
    path('<int:pk>/', views.lead_details, name='lead_details'),
    path('<int:pk>/edit/', views.lead_edit , name='lead_edit'),
    path('<int:pk>/delete/', views.delete_lead, name='delete_lead'),
    path('<int:pk>/convert/', views.convert_to_client, name='convert_to_client'),
    path('update/bulk/', views.update_status_priority_bulk, name='update_status_priority_bulk'),
]