from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from snippets.models import Guestnote
from snippets.serializers import GuestnoteModelSerializer

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

"""
@api_view(['GET', 'POST'])
def guestnote_list(request, format=None):
    if request.method == 'GET':
        snippets = Guestnote.objects.all()
        serializer = GuestnoteModelSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = GuestnoteModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""


class GuestnoteList(APIView):
    """
    list all guestnotes or generate a new one
    """
    def get(self, request, format=None):
        """
        List all guestnotes
        """
        snippets = Guestnote.objects.all()
        serializer = GuestnoteModelSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        Generate a new guestnote
        """
        serializer = GuestnoteModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class GuestnoteList2(generics.GenericAPIView):
    serializer_class = GuestnoteModelSerializer
    """
    list all guestnotes or generate a new one
    """
    def get(self, request, format=None):
        """
        List all guestnotes
        """
        snippets = Guestnote.objects.all()
        serializer = GuestnoteModelSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        Generate a new guestnote
        """
        serializer = GuestnoteModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GuestnoteList3(generics.ListCreateAPIView):
    queryset = Guestnote.objects.all()
    serializer_class = GuestnoteModelSerializer



@api_view(['GET', 'PUT', 'DELETE'])
def guestnote_detail(request, pk, format=None):
    """
    Retrieve, update or delete a guest note.
    """
    try:
        snippet = Guestnote.objects.get(pk=pk)
    except Guestnote.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GuestnoteModelSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = GuestnoteModelSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

