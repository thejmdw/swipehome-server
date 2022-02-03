"""View module for handling requests about park areas"""
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from swipehomeapi.models import AppUser


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

