from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import plasticSerializer
from vdeed_app.models import plastic

# Create your views here.


@api_view(['GET'])
def view_api(request):
    api_urls = {
        'List': '/task-list/',
    }
    return Response(api_urls)


@api_view(['GET'])
def view_plastic_counters(request):
    counters = plastic.objects.all()
    serializer = plasticSerializer(counters, many=True)
    return Response(serializer.data)
