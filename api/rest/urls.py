from .import views
from django.urls import path
urlpatterns = [
     path('',views.apiAvailable,name='apiAvailable'),
     path('taskList/',views.apiList,name='apiList'),
     path('taskDetail/<str:pk>/',views.apiDetail,name='apiDetail'),
     path('taskCreate/',views.apiCreate,name='apiCreate'),
     path('taskUpdate/<str:pk>/',views.apiUpdate,name='apiUpdate'),
       path('taskDelete/<str:pk>/',views.apiDelete,name='apiDelete'),
    
]
