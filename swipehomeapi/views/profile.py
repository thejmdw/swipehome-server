"""View module for handling requests about park areas"""
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from swipehomeapi.models import AppUser, UserType


class Profile(ViewSet):
    """AppUser can see profile information"""

    def list(self, request):
        """Handle GET requests to profile resource

        Returns:
            Response -- JSON representation of user info and events
        """
        app_user = AppUser.objects.get(user=request.auth.user)
        # events = EventSerializer(
        #     events, many=True, context={'request': request})
        app_user = AppUserSerializer(
            app_user, many=False, context={'request': request})

        # Manually construct the JSON structure you want in the response
        profile = {}
        profile["app_user"] = app_user.data
        # profile["events"] = events.data

        return Response(profile)
    
    def update(self, request, pk=None):
        """
        @api {PUT} /appusers/:id PUT changes to AppUser profile
        @apiName UpdateAppUser
        @apiGroup AppUser

        @apiHeader {String} Authorization Auth token
        @apiHeaderExample {String} Authorization
            Token 9ba45f09651c5b0c404f37a2d2572c026c146611

        @apiParam {id} id AppUser Id to update
        @apiSuccessExample {json} Success
            HTTP/1.1 204 No Content
        """
        app_user = AppUser.objects.get(user=request.auth.user)
        app_user.user.first_name = request.data["first_name"]
        app_user.user.last_name = request.data["last_name"]
        app_user.user.username = request.data["username"]
        app_user.avatarURL = request.data["avatarURL"]
        app_user.userType = UserType.objects.get(id=request.data["userType"])
        app_user.user.save()
        app_user.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

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
        fields = ('user', 'avatarURL', 'userType', 'firstTimeUser')

