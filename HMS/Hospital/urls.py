from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='index'),
    path('about/',views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/',views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('view_doctor/', views.view_Doctor, name='view_doctor'),
    path('add_doctor/', views.add_Doctor, name='add_doctor'),
    path('delete_doctor(?p<int:pid>)',views.Delete_Doctor, name='delete_doctor'),
    path('view_patient/',views.view_Patient, name="view_patient"),
    path('delete_patient(?p<int:pid>)', views.Delete_Patient, name="delete_patient"),
    path('add_patient/',views.add_Patient, name="add_patient"),
    path('add_appointment/', views.add_Appointment, name="add_appoinment"),
    path('view_appointment/', views.view_Appointment, name="view_appoinment"),
    path('delete_appointment(?p<int:pid>)', views.Delete_Appointment, name="delete_appointment"),
]