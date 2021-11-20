from rest_framework import serializers

from search.models import ResultModel

class ResultModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=ResultModel
        fields=('title', 'description', 'pubdate', 'thumb')
        