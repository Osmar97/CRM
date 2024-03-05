
from django.contrib import admin
from django.urls import path, include
from core.views import index ,about
from userprofile.views import registrar
from django.contrib.auth import views

urlpatterns = [
    path('',index, name="index"),
    path('dashboard/lead/add-lead', include ('lead.urls')),
    path('dashboard/lead/show-lead', include ('lead.urls')),
    path('dashboard/lead/', include ('lead.urls')),
    path('dashboard/clients/', include ('client.urls')),
    path('dashboard/', include ('dashboard.urls')),
    path('about/',about, name="about"),
    path('registrar/',registrar, name="registrar"),
    path('login/', views.LoginView.as_view(template_name='userprofile/login.html'),name='login'),
    path('logout/',views.LogoutView.as_view(),name='logout'),
    path('admin/', admin.site.urls),
]
