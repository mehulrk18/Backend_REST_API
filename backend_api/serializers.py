from rest_framework import serializers


class TestSerializer(serializers.Serializer):
    """Test Serializer for name field"""
    name = serializers.CharField(max_length=10)
