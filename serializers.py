from rest_framework import serializers
from .models import Notes


class NotesSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Notes
        fields = ('id', 'title', 'content', 'owner', 'created_at', 'updated_at')
