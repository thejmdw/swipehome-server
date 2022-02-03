"""
   Author: Daniel Krusch
   Purpose: To convert product type data to json
   Methods: GET, POST
"""

"""View module for handling requests about product categories"""
from django.contrib.auth.models import User
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from swipehomeapi.models import Message, AppUser
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for app_user's related Django user"""
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username')

class AppUserSerializer(serializers.ModelSerializer):
    """JSON serializer for app_users"""
    user = UserSerializer(many=False)

    class Meta:
        model = AppUser
        fields = ('user',)
        
class MessageSerializer(serializers.ModelSerializer):
    """JSON serializer for product type"""
    app_user = AppUserSerializer(many=False)
    
    class Meta:
        model = Message
        # url = serializers.HyperlinkedIdentityField(
        #     view_name='search',
        #     lookup_field='id'
        # )
        fields = ('id', 'app_user', 'recipientId', 'text', 'timestamp', 'unread')


class Messages(ViewSet):
    """Categories for products"""
    # permission_classes = (IsAuthenticatedOrReadOnly,)

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized product type instance
        """
        new_message = Message()
        new_message.app_user = AppUser.objects.get(user=request.auth.user)
        new_message.recipientId = request.data["recipientId"]
        new_message.text = request.data["text"]
        new_message.timestamp = request.data["timestamp"]
        new_message.unread = request.data["unread"]
        new_message.save()

        serializer = MessageSerializer(new_message, context={'request': request})

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        """
        @api {PUT} /products/:id PUT changes to product
        @apiName UpdateProduct
        @apiGroup Product

        @apiHeader {String} Authorization Auth token
        @apiHeaderExample {String} Authorization
            Token 9ba45f09651c5b0c404f37a2d2572c026c146611

        @apiParam {id} id Product Id to update
        @apiSuccessExample {json} Success
            HTTP/1.1 204 No Content
        """
        


        message = Message.objects.get(pk=pk)
        message.city = request.data["city"]
        message.text = request.data["text"]
        message.timestamp = request.data["timestamp"]
        message.unread = request.data["unread"]
        message.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single search"""
        try:
            message = Message.objects.get(pk=pk)
            serializer = MessageSerializer(message, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to Topping resource"""
        
        app_user = AppUser.objects.get(user=request.auth.user.id)
        message = Message.objects.filter(app_user=app_user)

        # Support filtering Toppings by area id
        # name = self.request.query_params.get('name', None)
        # if name is not None:
        #     ProductCategories = ProductCategories.filter(name=name)

        serializer = MessageSerializer(
            message, many=True, context={'request': request})
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        """
        @api {DELETE} /products/:id DELETE product
        @apiName DeleteProduct
        @apiGroup Product

        @apiHeader {String} Authorization Auth token
        @apiHeaderExample {String} Authorization
            Token 9ba45f09651c5b0c404f37a2d2572c026c146611

        @apiParam {id} id Product Id to delete
        @apiSuccessExample {json} Success
            HTTP/1.1 204 No Content
        """
        try:
            message = Message.objects.get(pk=pk)
            message.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Message.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
