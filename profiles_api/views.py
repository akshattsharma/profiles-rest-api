from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status, viewsets

from profiles_api import serializers

class HelloApiView(APIView):
    """Test API view"""
    serializer_class= serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = {
            'Uses HTTP methods as fuction (get, post, patch, put,delete)',
            'Is similar to a traditional django view',
            'Gives you the most control over your app logic',
            'Is mapper manually to URLs',
        }

        return Response({'message': 'Hello', 'an_apiview' : an_apiview})
    

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message' : message})
        else:
            return Response(serializer.errors, 
                            status = status.HTTP_400_BAD_REQUEST)
        

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method' : 'PUT'})
    
    def patch(self, request, pk=None):
        """Handles a partial update"""
        return Response({'method' : 'Patch'})
    
    def delete(self, request, pk=None):
        return Response({'method' : 'Delete'})


class HelloViewSet(viewsets.ViewSet):
    """Test API viewsets"""
    serializer_class = serializers.HelloSerializer
    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            'Uses actions(list, create, retreive, update, partial update)',
            'Automatically maps to urls using routers',
            'Provides more functianality with less code',
        ]

        return Response({'message' : 'Hello!', 'a_viewset': a_viewset})
    
    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response ({'message' : message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        
    def retrieve(self, request, pk=None):
        """Handle gettign an object by getting its id"""
        return Response({'http_method' : 'GET'})
    
    def update(self, request, pk=None):
        """Handle updating an objecr"""
        return Response({'http_method' : 'PUT'})
    
    def partial_update(self, request, pk=None):
        """Handling updating part of an object"""
        return Response({'http_method': 'PATCH' })
    
    def destroy(self, request, pk=None):
        """Handling deleting the object"""
        return Response({'http_method': 'DELETE'})
