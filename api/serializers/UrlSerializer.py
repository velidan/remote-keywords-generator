from rest_framework import serializers
from api.models import Url

class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ['id', 'address', 'title', 'keywords']
        extra_kwargs = {
                        'address': {'required': False},
                        'title': {'required': False}
                        }

    def create(self, validated_data):
        url, created = Url.objects.update_or_create(
            address=validated_data.get('address', None),
            defaults={'title': validated_data.get('title', None),
                      'keywords': validated_data.get('keywords', None),})
        return url