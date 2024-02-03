from django.db import models
from djongo.models.fields import ListField

class Webhook(models.Model):
    company_id = models.CharField(max_length=200)
    url = models.URLField()
    headers = models.JSONField()
    events = ListField(models.CharField(max_length=200))
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_id