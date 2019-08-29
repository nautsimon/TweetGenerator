from rest_framework import serializers
from gen.models import Gen, LANGUAGE_CHOICES, STYLE_CHOICES


class GenSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    handle = serializers.CharField(
        required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(
        style={'base_template': 'textarea.html'}, required=False)
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(
        choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Gen.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.handle = validated_data.get('handle', instance.handle)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
