from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from backend_api import serializers


class TestAPIView(APIView):
    """Testing APIView"""
    serializer_class = serializers.TestSerializer

    def get(self, request, format=None):
        """ Returns List of APIView Features"""
        api_response = [
            "Uses HTTP MEthods as Functions",
            "Similar to Traditional Django",
            "Gives most control Over your Application logic",
            "Is mapped manually to URLs",
        ]

        return Response({'message':'Hello', 'api_response': api_response}) # JSON Style.

    def post(self, request):
        """Creating Post for Name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({"message" : message})

        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def put(self, request,  pk=None):
        """For Updating object with primary key"""
        return Response({"method":"PUT"})

    def patch(self, request,  pk=None):
        """For Updating an object attribute with primary key"""
        return Response({"method":"PATCH"})

    def delete(self, request,  pk=None):
        """For Deleting object with primary key"""
        return Response({"method":"DELETE"})
