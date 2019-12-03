"""
View to handle a single URL. Details, Update, Delete
"""

from django.http import Http404

from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import certifi
import urllib3
from bs4 import BeautifulSoup

from api.models import Url
from api.serializers import UrlSerializer

class UrlView(APIView):
    """
    handles a single URL
    """
    def getObjects(self, url):
        try:
            # TODO: by Url
            return Url.objects.get(address=url)
        except Url.DoesNotExist:
            raise Http404
    
    def get(self, request, url, format=None):
        url_keywords = self.getObjects(url)
        serializer = UrlSerializer(url_keywords)
        return Response(serializer.data)
    
    def put(self, request, url, format=None):
        url_keywords = self.getObjects(url)
        serializer = UrlSerializer(url_keywords, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, url, format=None):
        url_keywords = self.getObjects(url)
        url_keywords.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)