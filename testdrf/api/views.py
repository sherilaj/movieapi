from django.shortcuts import render

from . serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
# Create your views here.
@api_view(['GET'])
def MovieList(request):
    mov = Movie.objects.all()
    serializer = MovieSerializer(mov,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def CommentList(request):
    com = Comment.objects.all()
    serializer = CommentSerializer(com, many=True)
    return Response(serializer.data)

class CreateUser(generics.CreateAPIView):
    model = get_user_model()
    serializer_class = UserSerializer
class CreateComment(generics.CreateAPIView):
    model = Comment
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated, )
@api_view(['GET'])
def Movie_Comment(request,forkey_id):
    com = Comment.objects.filter(forkey_id=forkey_id)
    serializer = CommentSerializer(com,many=True)
    return Response(serializer.data)