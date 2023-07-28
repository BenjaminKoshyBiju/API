from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task

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

@api_view(['GET'])
def apiList(request):
    tasks=Task.objects.all()
    serializer=TaskSerializer(tasks, many=True) 
    return Response(serializer.data)

@api_view(['GET'])
def apiDetail(request,pk):
    tasks=Task.objects.get(id=pk)
    serializer=TaskSerializer(tasks, many=False) 
    return Response(serializer.data)


@api_view(['POST'])
def apiCreate(request):
    serializer=TaskSerializer(data=request.data)

    if serializer.is_valid():
     serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def apiUpdate(request,pk):
    task=Task.objects.get(id=pk)
    serializer=TaskSerializer(instance=task,data=request.data) 

    if serializer.is_valid():
     serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def apiDelete(request,pk):
    task=Task.objects.get(id=pk)
    task.delete()
    
    return Response("Deleted Successfully!")



