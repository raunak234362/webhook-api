from django.urls import path, include
from rest_framework.routers import DefaultRouter
from webhook_api.views import WebhookViewSet

# from webhook import webhook_api


router = DefaultRouter()
router.register(r'Webhooks', WebhookViewSet, basename='webhooks')

urlpatterns = [
    path('',include(router.urls)),
]