from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from snippets.models import Guestnote
from snippets.serializers import GuestnoteModelSerializer

@csrf_exempt
def guestnote_list(request):
    """
    List all guest notes, or create a new guest note
    """
    if request.method == 'GET':
        snippets = Guestnote.objects.all()
        serializer = GuestnoteModelSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = GuestnoteModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def guestnote_detail(request, pk):
    """
    Retrieve, update or delete a guest note.
    """
    try:
        snippet = Guestnote.objects.get(pk=pk)
    except Guestnote.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = GuestnoteModelSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = GuestnoteModelSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)
