from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import serializers
from .serializers import TodoSerializer
from .models import Todo

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
def home(request):
    return HttpResponse('<center><h1 style="background-color:powderblue;">Welcome to ApiTodo</h1></center>')


@api_view(['GET'])
def todoList(request):
    querset = Todo.objects.all()
    
    serializer = TodoSerializer(querset, many=True)
    
    return Response(serializer.data)

@api_view(['POST'])
def todoListCreate(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
