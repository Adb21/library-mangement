from django.urls import path
from . import views

urlpatterns = [
    path('admin',views.RegisterAdminAPIView.as_view(), name='adminRegister'),
    path('student',views.RegisterStudentAPIView.as_view(), name='studentRegister'),
    path('login',views.LoginAPIView.as_view(), name='login'),
    path('logout',views.LogoutAPIView.as_view(), name='logout'),
]