from django.urls import path,include
from .views import UserProfileView,ListPatientAPIView,CreatePatientAPIView,UpdatePatientAPIView,DeletePatientAPIView

urlpatterns = [
	path('profile/',UserProfileView.as_view()),
	path("patient/all/",ListPatientAPIView.as_view(),name="todo_list"),
    path("create/patient/", CreatePatientAPIView.as_view(),name="todo_create"),
    path("update/patient/<int:pk>/",UpdatePatientAPIView.as_view(),name="update_todo"),
    path("delete/patient/<int:pk>/",DeletePatientAPIView.as_view(),name="delete_todo")
	
	
]