from rest_framework.views import APIView
from rest_framework.response import Response


class TestAPIView(APIView):
    """Testing APIView"""

    def get(self, request, format=None):
        """ Returns List of APIView Features"""
        api_response = [
            "Uses HTTP MEthods as Functions",
            "Similar to Traditional Django",
            "Gives most control Over your Application logic",
            "Is mapped manually to URLs",
        ]

        return Response({'message':'Hello', 'api_response': api_response}) # JSON Style.
