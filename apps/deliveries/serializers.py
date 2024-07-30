"""Serializers for Deliveries App."""

from rest_framework import serializers


class FailedDeliverySerializer(serializers.Serializer):
    """Serializer for recording failed deliveries."""

    reason = serializers.CharField(required=True, max_length=255)


class SignatureSerializer(serializers.Serializer):
    """Serializer for validating delivery signatures."""

    signature = serializers.ImageField(required=True)
