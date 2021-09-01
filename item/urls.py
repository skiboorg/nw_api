from django.urls import path,include
from . import views

urlpatterns = [
    path('get_items', views.GetItems.as_view()),





]

