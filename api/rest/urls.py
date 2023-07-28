from .import views
from django.urls import path
urlpatterns = [
     path('',views.apiAvailable,name='apiAvailable'),
    #  path('modify/<str:note_id>/',views.modify.as_view(),name='mod'),
    
]
