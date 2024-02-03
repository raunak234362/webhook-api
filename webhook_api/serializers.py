from rest_framework import serializers
from .models import Webhook

class WebhookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Webhook
        fields = ('company_id', 'url', 'headers', 'events', 'is_active', 'created_at', 'updated_at')
        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }

    headers = serializers.JSONField(required=False)
    events = serializers.ListField(child=serializers.CharField())
