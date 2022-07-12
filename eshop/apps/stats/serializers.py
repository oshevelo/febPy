from rest_framework import serializers
from .models import UserAction


class UserActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAction
        fields = '__all__'


class UserActionNestedSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = UserAction
        read_only_fields = ['pub_date', 'data']
        fields = read_only_fields + ['id']


# authentication_classes = (SessionAuthentication, BasicAuthentication)
# permission_classes = (IsAuthenticated,)
