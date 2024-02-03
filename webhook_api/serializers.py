from rest_framework import serializers
from .models import Webhook

from djongo.models.fields import ListField

class WebhookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Webhook
        fields = ('company_id', 'url', 'headers', 'events', 'is_active', 'created_at', 'updated_at')
        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }

    events = ListField(child=serializers.CharField(max_length=200))