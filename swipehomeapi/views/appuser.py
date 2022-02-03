from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from swipehomeapi.models import AppUser


class AppUserSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for AppUsers"""
    class Meta:
        model = AppUser
        url = serializers.HyperlinkedIdentityField(
            view_name='AppUser', lookup_field='id'
        )
        fields = ('id', 'url', 'user', 'avatarURL', 'userType', 'firstTimeUser')
        depth = 1


class AppUsers(ViewSet):

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
        app_user.user.email = request.data["email"]
        app_user.avatarURL = request.data["avatarURL"]
        app_user.userType = request.data["userType"]
        app_user.user.save()
        app_user.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

