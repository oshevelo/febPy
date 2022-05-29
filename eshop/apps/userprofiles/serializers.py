from rest_framework import serializers

from django.contrib.auth.models import User

from .models import UserProfile


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    # def validate_password(self):

    def create(self, validated_data):
        user = User.objects.create(**validated_data, is_active=False)
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    username = serializers.CharField(source='user.username')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')

    class Meta:
        model = UserProfile
        # fields = '__all__'
        fields = ['username', 'first_name', 'last_name',
                  'date_of_birth', 'sex', 'preferable_language', 'addresses_of_delivery',
                  'telephones', 'additional_emails']

    def update(self, instance, validated_data):
        # user = User.objects.get(id=instance.user_id)
        user = self.context['request'].user

        user_data = None
        if 'user' in validated_data:
            user_data = validated_data.pop('user')
        if user_data:
            for key, value in user_data.items():
                setattr(user, key, value)
            user.save()

        if validated_data:
            for key, value in validated_data.items():
                setattr(instance, key, value)
            instance.save()

        return instance

