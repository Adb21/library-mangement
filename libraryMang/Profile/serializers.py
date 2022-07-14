import email
from operator import mod
from rest_framework import serializers
from django.contrib.auth.models import User,update_last_login
from django.contrib.auth import authenticate,login
from rest_framework_simplejwt.tokens import RefreshToken,TokenError


class AdminSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length = 50, min_length = 8, write_only = True)
    email = serializers.EmailField(max_length = 50)
    first_name = serializers.CharField(max_length = 100)
    last_name = serializers.CharField(max_length = 100)

    class Meta:
        model = User
        fields = ('username', 'email','password', 'first_name', 'last_name')

    def validate(self, attrs):
        mail = attrs['email']
        if User.objects.filter(email=mail).exists():
            msg = {"email error":"Email Already Exists"}
            raise serializers.ValidationError(msg)
        return super().validate(attrs)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user

class StudentSerailizer(serializers.ModelSerializer):
    password = serializers.CharField(max_length = 50, min_length = 8, write_only = True)
    email = serializers.EmailField(max_length = 50)

    class Meta:
        model = User
        fields = ('username', 'email','password')

    def validate(self, attrs):
        mail = attrs['email']
        if User.objects.filter(email=mail).exists():
            msg = {"email error":"Email Already Exists"}
            raise serializers.ValidationError(msg)
        return super().validate(attrs)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.save()
        return user


class LoginSerailizer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length = 50)

    class Meta:
        model = User
        fields = ['email','password']

    def validate(self, attrs):
        email = attrs["email"]
        password = attrs["password"]
        print(self.context.get('request'))
        user = authenticate(request=self.context.get('request'),username=email, password=password)
        print(user)
        if user is None:
            msg = {"User error":"Invalid Credentials. User Not Found"}
            raise serializers.ValidationError(msg)
        print(type(user))
        update_last_login(None, user)

        return super().validate(attrs)

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):

        try:
            RefreshToken(self.token).blacklist()

        except TokenError:
            msg = {
                'bad_token': 'Token is expired or invalid'
            }
            raise serializers.ValidationError(msg)

def getTokens(email):
    if User.objects.filter(email=email).exists():
        userObj = User.objects.get(email=email)
        tokens = RefreshToken.for_user(userObj)
        refresh = str(tokens)
        access = str(tokens.access_token)
        data = {
            "refresh": refresh,
            "access": access
        }
        return data
    return None