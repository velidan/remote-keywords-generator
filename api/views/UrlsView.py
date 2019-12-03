"""
The view could render the all previously saved urls 
or creates the keywords for the new one if it isn't existing
"""

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import Url
from api.serializers import UrlSerializer
from api.services import getKeywordsForUrl, UrlDoesntExists

class UrlsView(APIView):
    """
    returns all urlKeywords entities or creates the the url and keywords for it
    """
    def get(self, request):
        keywords = Url.objects.all()
        serializer = UrlSerializer(keywords, many=True)
        return Response(serializer.data)

    def post(self, request):
        requested_url = request.data['url']
        
        try:
            url_keywords = getKeywordsForUrl(requested_url)
        except UrlDoesntExists as e:
            return Response(str(e), status=status.HTTP_404_NOT_FOUND)

        serializer = UrlSerializer(data={'address':  requested_url,
                                         'keywords': url_keywords} )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
