"""
View to handle a single URL by id. Details, Update, Delete
"""

from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.models import Url
from api.serializers import UrlSerializer

class UrlView(APIView):
    """
    Provides a RUD api for a single url requesta
    """
    def getObjects(self, pk):
        try:
            return Url.objects.get(pk=pk)
        except Url.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        url_entity = self.getObjects(pk)
        serializer = UrlSerializer(url_entity)
        return Response(serializer.data)
    
    def put(self, request, pk):
        url_entity = self.getObjects(pk)
        serializer = UrlSerializer(url_entity, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        url_entity = self.getObjects(pk)
        url_entity.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)