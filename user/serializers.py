from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from userprofile.models import LabtechProfile, NurseProfile,InrRangeProfile, PaitentProfile,DoctorProfile, ReceptionProfile
from user.models import User


JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER

# labtech
class LabTechSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabtechProfile
        fields = ['full_name']
# reception


class ReceptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceptionProfile
        fields = ['full_name']




 

    
class PaitentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaitentProfile
        fields = ('first_name', 'last_name', 'phone_number', 'age', 'gender','case')

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorProfile
        fields = ['full_name']

class NurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = NurseProfile
        fields = ['full_name','phone_number','gender']



# lab tech

class LabTechRegistrationSerializer(serializers.ModelSerializer):

    profile = LabTechSerializer(required=False)

    class Meta:
        model = User
        fields = ('email', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create_labtechuser(**validated_data)
        LabtechProfile.objects.create(
            user=user,
            full_name=profile_data['full_name'],
        )
        return user

# reception

class ReceptionRegistrationSerializer(serializers.ModelSerializer):

    profile = ReceptionSerializer(required=False)

    class Meta:
        model = User
        fields = ('email', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create_receptionistuser(**validated_data)
        ReceptionProfile.objects.create(
            user=user,
           full_name=profile_data['full_name'],
        )
        return user

class DoctorRegistrationSerializer(serializers.ModelSerializer):

    profile = DoctorSerializer(required=False)

    class Meta:
        model = User
        fields = ('email', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create_doctoruser(**validated_data)
        DoctorProfile.objects.create(
            user=user,
            full_name=profile_data['full_name'],
            
        )
        return user


class NurseRegistrationSerializer(serializers.ModelSerializer):

    profile = NurseSerializer(required=False)

    class Meta:
        model = User
        fields = ('email', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create_nurseuser(**validated_data)
        NurseProfile.objects.create(
            user=user,
            full_name=profile_data['full_name'],

            
            
            
        )
        return user

class PaitentAddSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaitentProfile
        fields = '__all__'


class InrAddSerializer(serializers.ModelSerializer):
  

    class Meta:
        model = InrRangeProfile
        fields = '__all__'

   

   

class UserLoginSerializer(serializers.Serializer):

    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)
        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password is not found.'
            )
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'User with given email and password does not exists'
            )
        return {
            'email':user.email,
            'token': jwt_token
        }



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model= User
        fields = ['is_paitent','is_doctor','is_nurse','is_receptionist','is_labtech']

