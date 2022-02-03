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
from swipehomeapi.models import Search, AppUser, UserType
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
        
class SearchSerializer(serializers.ModelSerializer):
    """JSON serializer for product type"""
    app_user = AppUserSerializer(many=False)
    
    class Meta:
        model = Search
        # url = serializers.HyperlinkedIdentityField(
        #     view_name='search',
        #     lookup_field='id'
        # )
        fields = ('id', 'city', 'state_code', 'postal_code', 'app_user', 'userType')


class Searches(ViewSet):
    """Categories for products"""
    # permission_classes = (IsAuthenticatedOrReadOnly,)

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized product type instance
        """
        new_search = Search()
        new_search.city = request.data["city"]
        new_search.state_code = request.data["state_code"]
        new_search.postal_code = request.data["postal_code"]
        new_search.app_user = AppUser.objects.get(user=request.data["app_user"])
        new_search.userType = UserType.objects.get(pk=request.data["userType"])
        new_search.save()

        serializer = SearchSerializer(new_search, context={'request': request})

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
        


        search = Search.objects.get(pk=pk)
        search.city = request.data["city"]
        search.state_code = request.data["state_code"]
        search.postal_code = request.data["postal_code"]
        search.app_user = AppUser.objects.get(app_user=request.data["app_user"])
        search.userType = request.data["userType"]
        search.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single search"""
        try:
            search = Search.objects.get(pk=pk)
            serializer = SearchSerializer(search, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to Topping resource"""
        
        app_user = AppUser.objects.get(user=request.auth.user.id)
        search = Search.objects.filter(app_user=app_user)

        # Support filtering Toppings by area id
        # name = self.request.query_params.get('name', None)
        # if name is not None:
        #     ProductCategories = ProductCategories.filter(name=name)

        serializer = SearchSerializer(
            search, many=True, context={'request': request})
        return Response(serializer.data)

    # def destroy(self, request, pk=None):
    #     """
    #     @api {DELETE} /products/:id DELETE product
    #     @apiName DeleteProduct
    #     @apiGroup Product

    #     @apiHeader {String} Authorization Auth token
    #     @apiHeaderExample {String} Authorization
    #         Token 9ba45f09651c5b0c404f37a2d2572c026c146611

    #     @apiParam {id} id Product Id to delete
    #     @apiSuccessExample {json} Success
    #         HTTP/1.1 204 No Content
    #     """
    #     try:
    #         search = Search.objects.get(pk=pk)
    #         search.delete()

    #         return Response({}, status=status.HTTP_204_NO_CONTENT)

    #     except Search.DoesNotExist as ex:
    #         return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    #     except Exception as ex:
    #         return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
