from django.db import models
from djongo.models.fields import ListField

class Webhook(models.Model):
    company_id = models.CharField(max_length=200, null=False)
    url = models.CharField(max_length=500, null=False)
    headers = models.JSONField(blank=True, null=True)
    events = ListField(models.CharField(max_length=200))
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Webhook for Company {self.company_id}"

    def to_json(self):
        # Custom JSON serialization for datetime fields
        return {
            'company_id': self.company_id,
            'url': self.url,
            'headers': self.headers,
            'events': self.events,
            'is_active': self.is_active,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
        }