from django.urls import path
from . import views
urlpatterns = [
         path('', views.index),
         path("reg/", views.student_registration, name="student_registration"),
         path("log/", views.student_login, name="student_login"),
         path("profile/", views.profile, name="profile"),
         path("logout/", views.profile, name="profile"),
         path("pass/", views.change_password, name="change_password"),
]
