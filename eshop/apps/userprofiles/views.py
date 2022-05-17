from rest_framework import generics, status
from rest_framework.response import Response
from django.http import Http404
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from .serializers import UserProfileSerializer, UserCreateSerializer
from .models import UserProfile


# class UserProfileList(generics.ListAPIView):
#     queryset = UserProfile.objects.all()
#     serializer_class = UserProfileSerializer


class UserProfileDetail(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get_object(self):
        if self.request.user.is_authenticated:
            return get_object_or_404(UserProfile,
                                     user=self.request.user)
        else:
            raise Http404


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    # def post(self, request, *args, **kwargs):
        # print('Hello from POST method')
        # print(f'self={self}')
        # print(f'args={args}')
        # print(f'kwargs={kwargs}')
        # result = super().post(*args, **kwargs)
        # send_email

        # return result

        # user = None
        # try:
        #     user = User.objects.get(username=request.data.get('username'))
        # except:
        #     print(f'except, user={user}')
        #     serializer = UserCreateSerializer(data=request.data)
        #     if serializer.is_valid():
        #         serializer.save()
        #         return Response(serializer.data, status=status.HTTP_201_CREATED)
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # else:
        #     print('user exists')
        #     return Response(f'User {user.username} already exists!', status=status.HTTP_400_BAD_REQUEST)
