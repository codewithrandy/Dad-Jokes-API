from rest_framework import serializers
from .models import DadJoke

class DadJokeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DadJoke
        fields = ['id', 'category', 'setup', 'punchline']