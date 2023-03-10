from rest_framework import serializers

from User.models import CustomUser


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name','username','date_of_birth'] # 'spouse_name',

