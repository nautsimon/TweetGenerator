from rest_framework import serializers

from generates.models import Generate


class GenerateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Generate
        fields = ('id', 'title', 'content')
