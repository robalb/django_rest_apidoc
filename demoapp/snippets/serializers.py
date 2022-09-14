from rest_framework import serializers
from snippets.models import Guestnote, LANGUAGE_CHOICES


class GuestnoteSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    note = serializers.CharField(style={'base_template': 'textarea.html'})
    like_tiangolo = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')

    def create(self, validated_data):
        """
        Create and return a new `Guestnote` instance, given the validated data.
        """
        return Guestnote.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Guestnote` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.note = validated_data.get('note', instance.note)
        instance.like_tiangolo = validated_data.get('like_tiangolo', instance.like_tiangolo)
        instance.language = validated_data.get('language', instance.language)
        instance.save()
        return instance


class GuestnoteModelSerializer(serializers.ModelSerializer):
  class Meta:
    model = Guestnote
    fields = ['id', 'title', 'note', 'like_tiangolo', 'language']
