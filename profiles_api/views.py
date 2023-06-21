from rest_framework.views import APIView
from rest_framework.views import Response

class HelloApiView(APIView):
    """Test API view"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = {
            'Uses HTTP methods as fuction (get, post, patch, put,delete)',
            'Is similar to a traditional django view',
            'Gives you the most control over your app logic',
            'Is mapper manually to URLs',
        }

        return Response({'message': 'Hello', 'an_apiview' : an_apiview})