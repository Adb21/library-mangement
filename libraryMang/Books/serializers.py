from rest_framework import serializers
from .models import Books
from django.contrib.auth.models import User

#QueryFieldsMixin : helps in retriving selected data 
class BookSerailizer(serializers.ModelSerializer):
    class Meta :
        model = Books
        fields = '__all__'
        
    def validate(self, attrs):
        request = self.context.get('request')
        username = request.session['username']
        user = User.objects.get(username=username)
        if not user.is_superuser:
            print("NOT SUPERUSER")
            msg = {"user error":"Not Admin"}
            raise serializers.ValidationError(msg)

        return super().validate(attrs)

