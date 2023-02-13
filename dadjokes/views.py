from django.http import JsonResponse
from .models import DadJoke
from .serializers import DadJokeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework import filters


@api_view(['GET', 'POST'])
def dadjoke_list(request, format=None):
    if request.method == 'GET':
        dadjokes = DadJoke.objects.all()
        serializer = DadJokeSerializer(dadjokes, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = DadJokeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def dadjoke_detail(request, id, format=None):
    try:
        dadjoke = DadJoke.objects.get(pk=id)
    except DadJoke.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DadJokeSerializer(dadjoke)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DadJokeSerializer(dadjoke, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        dadjoke.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

class DadJokesAPIView(generics.ListCreateAPIView):
    search_fields = ['category']
    filter_backends = (filters.SearchFilter,)
    queryset = DadJoke.objects.all()
    serializer_class = DadJokeSerializer