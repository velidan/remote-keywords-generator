from rest_framework.views import APIView
from rest_framework.response import Response

import certifi
import urllib3
from bs4 import BeautifulSoup

from api.models import Url
from api.serializers import UrlSerializer

class UrlsView(APIView):
    """
    returns all urlKeywords entities
    """
    def get(self, request, format=None):
        keywords = Url.objects.all()
        serializer = UrlSerializer(keywords, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        requested_url = request.data['url']

        # adding ssl certificates
        http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',
                                    ca_certs=certifi.where())

        response = http.request('GET', requested_url)
        soup = BeautifulSoup(response.data, 'html.parser')
        print(soup.title.string)
        return Response('functionality is coming soon but the title IS -> {0}'.format(soup.title.string))
        # serializer = UrlKeywordsSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)