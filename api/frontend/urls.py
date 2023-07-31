from .import views
from django.urls import path
urlpatterns = [
     path('',views.list,name='list'),
     path('login/', views.login_view, name='login'),
    
]