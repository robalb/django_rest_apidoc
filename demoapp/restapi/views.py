from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from restapi.models import Guestnote
from restapi.serializers import GuestnoteModelSerializer

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

# DRF APIView class ---> No introspection available
class GuestnoteList1(APIView):
    """
    list all guestnotes or generate a new one

    No introspection
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



# APIVIew class has been replaced with generics class, introspection
# is available via serializer_class and queryset
class GuestnoteList2(generics.GenericAPIView):
    """
    list all guestnotes or generate a new one

    Manual introspection
    """
    serializer_class = GuestnoteModelSerializer
    queryset = Guestnote.objects.all()

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


# DRF mixin generics class -> Good introspection available by default
class GuestnoteList3(generics.ListCreateAPIView):
    """
    list all guestnotes or generate a new one

    Automatic introspection
    """
    queryset = Guestnote.objects.all()
    serializer_class = GuestnoteModelSerializer



# DRF default @api_view decorator ---> No introspection available
@api_view(['GET', 'PUT', 'DELETE'])
def guestnote_detail(request, pk, format=None):
    """
    Retrieve, update or delete a guest note.

    No introspection
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

