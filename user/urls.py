from django.urls import path,include
from .views import PaitentRegistrationView,DoctorRegistrationView,UserLoginView,NurseRegistrationView

urlpatterns = [
	path('signup/paitent/',PaitentRegistrationView.as_view(),name='signup_paitent'),
	path('signup/doctor/',DoctorRegistrationView.as_view(),name='signup_doctor'),
	path('signup/nurse/',NurseRegistrationView.as_view(),name='signup_nurse'),
	path('signin/',UserLoginView.as_view()),
]