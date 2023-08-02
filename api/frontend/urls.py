from .import views
from django.urls import path
urlpatterns = [
     path('list/',views.list,name='list'),
     path('', views.login_view, name='login'),
     path('register/', views.register_view, name='register'),
    
]