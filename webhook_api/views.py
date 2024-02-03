from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Webhook
from .serializers import WebhookSerializer


class WebhookViewSet(viewsets.ModelViewSet):
    queryset = Webhook.objects.all()
    serializer_class = WebhookSerializer

    @api_view(['GET'])
    def listing(request):
        webhooks = Webhook.objects.all()
        serializer = WebhookSerializer(webhooks, many=True)
        return Response(serializer.data)

    @api_view(['GET'])
    def single_get(request, pk):
        webhook = Webhook.objects.get(id=pk)
        serializer = WebhookSerializer(webhook)
        return Response(serializer.data)

    @api_view(['POST'])
    def create(request):
        serializer = WebhookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)  # Return 201 Created for successful POST
        return Response(serializer.errors, status=400)  # Return 400 Bad Request for invalid data

    @api_view(['PATCH'])
    def update(request, pk):
        webhook = Webhook.objects.get(id=pk)
        serializer = WebhookSerializer(webhook, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    @api_view(['DELETE'])
    def delete(request, pk):
        webhook = Webhook.objects.get(id=pk)
        webhook.delete()
        return Response(status=204)