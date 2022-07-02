from django.urls import path, include
# from django.contrib.auth import get_user_model
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from .models import Patient, Doctor, Nurse, INR
from rest_framework import routers, serializers, viewsets
from rest_framework.permissions import IsAuthenticated

# Serializers define the API representation.
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = get_user_model()
#         fields = ['url', 'username', 'email', 'is_staff' ,'is_receptionist' ,'is_nurse' ,'is_labtech' ,'is_doctor']

# # ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
# patient
class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = ['url','id','Patient_name', 'Patient_age', 'Patient_Residence', 'Patient_phone', 'Patient_email', 'Patient_Bp', 'Patient_weight', 'Patient_height', 'Patient_temperature', 'Patient_Inr', 'Patient_Diagnosis']
class PatientViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = (IsAuthenticated,)
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


# doctor
class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doctor
        fields = ['url', 'username','password']

class DoctorViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = (IsAuthenticated,)
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer



class NurseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Nurse
        fields = ['url', 'username', 'password']
    

class NurseViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = (IsAuthenticated,)
    queryset = Nurse.objects.all()
    serializer_class = NurseSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'doctors', DoctorViewSet)
router.register(r'nurses', NurseViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]

    