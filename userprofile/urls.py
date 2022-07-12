from django.urls import path,include
from .views import UserProfileView,ListPatientAPIView,PatientRemedyAPIView,ListInrRangeAPIView,CreateInrRangeAPIView,CreatePatientAPIView,UpdatePatientAPIView,DeletePatientAPIView

urlpatterns = [
    # profile
	path('profile/',UserProfileView.as_view()),

    # patient
	path("patient/all/",ListPatientAPIView.as_view(),name="patient_list"),
    path("create/patient/", CreatePatientAPIView.as_view(),name="patient_create"),
    path("update/patient/<int:pk>/",UpdatePatientAPIView.as_view(),name="update_patient"),
    path("delete/patient/<int:pk>/",DeletePatientAPIView.as_view(),name="delete_patient"),

    # inr 

    path("inrrange/all/",ListInrRangeAPIView.as_view(),name="inr_list"),

    path("inrrange/add/",CreateInrRangeAPIView.as_view(),name="add_inr"),

    # doc get patient inr remedy

    path("getpatient/remedy/",PatientRemedyAPIView.as_view(),name="get_remedy")
	
	
]