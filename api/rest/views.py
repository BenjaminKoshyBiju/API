from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def apiAvailable(request):

    api_urls={
        'List':'/taskList',
        'Detailed View':'/taskDetail/<str:pk>',
        'Create':'/taskCreate/',
        'Update':'/taskUpdate/<str:pk>',
        'Delete':'/taskDelete/<str:pk>',

    }
    return Response(api_urls)

