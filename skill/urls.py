from django.urls import path,include
from . import views

urlpatterns = [
    path('weapons', views.GetWeapons.as_view()),
    path('weapon', views.GetWeapon.as_view()),

    path('build', views.Builds.as_view()),

    path('parse', views.ParceHtml.as_view()),



]
