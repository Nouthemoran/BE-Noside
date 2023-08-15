from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', '', 'email','password','username']
        extra_kwargs = {
            'password':{'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # Gunakan make_password untuk mengenkripsi password sebelum menyimpannya
        validated_data['password'] = make_password(password)
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance


        

