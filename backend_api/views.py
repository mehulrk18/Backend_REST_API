from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet


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



class TestViewSet(ViewSet):
    """Testing ViewSet for API"""
    serializer_class = serializers.TestSerializer

    def list(self, request):
        """List of Actions performed by ViewSet"""

        a_viewset = [
            "A View set performs actions (list, create, update, retrieve, destroy)",
            "Automatically maps urls using URL Router",
            "Proveides more functionality with less code"
        ]

        return Response({'message':'Hello, ', 'a_viewset': a_viewset})

    def create(self, request):
        """Creating an object """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello {name}!"
            return Response({'message': message})

        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk = None):
        """Retrieve information"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk = None):
        """Update object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk = None):
        """Partially updating Object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk = None):
        """Deleting an Object"""
        return Response({'http_method': 'DELETE'})
