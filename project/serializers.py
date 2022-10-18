from rest_framework import serializers
from django.contrib.auth.models import User
from .import models
# from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = ('first_name', 'second_name','date_of_graduation','date_of_employment','position','salary','supervisor','employee_code')



class RegisterSerializer(serializers.ModelSerializer):
   class Meta:
        model =models.Employee
        fields = ('first_name', 'second_name','date_of_employment','date_of_graduation','position','salary',)

       
    
password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
password2 = serializers.CharField(write_only=True, required=True)
class Meta:
    model = User
    fields = ('password', 'first_name', 'last_name',)
    extra_kwargs = {
      'first_name': {'required': True},
      'last_name': {'required': True},
      'password':  {'required': True}
    }
def validate(self, attrs):
    if attrs['password'] != attrs['password2']:
      raise serializers.ValidationError(
        {"password": "Password fields didn't match."})
    return attrs
def create(self, validated_data):
    user = User.objects.create(
      username=validated_data['username'],
      first_name=validated_data['first_name'],
      last_name=validated_data['last_name']
    )
    user.set_password(validated_data['password'])
    user.save()
    return user


