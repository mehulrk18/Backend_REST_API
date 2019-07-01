from rest_framework import serializers
from backend_api import models

class TestSerializer(serializers.Serializer):
    """Test Serializer for name field"""
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """User Profile Serializer"""

    class Meta:
        """Meta Class."""
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create a user in the User Profile Database"""

        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password']
        )

        return user
