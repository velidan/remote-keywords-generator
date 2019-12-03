from rest_framework import serializers
from api.models import Url

class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ['id', 'address', 'keywords']
        extra_kwargs = {'address': {'required': False}}