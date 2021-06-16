from django.urls import path,include
from . import views

urlpatterns = [
    path('items', views.Item.as_view()),
    path('cc', views.Craft.as_view()),

    path('banner', views.GetBanner.as_view()),
    path('faq', views.GetFaq.as_view()),


]

