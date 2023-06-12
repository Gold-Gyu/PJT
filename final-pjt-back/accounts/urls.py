from django.urls import path
from . import views

urlpatterns = [
  path("userinfo/<int:user_pk>/", views.userinfo),
  path("delete/", views.delete),
  
]