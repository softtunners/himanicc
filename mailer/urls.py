
from django.urls import path
from .views import *
urlpatterns = [
    path('mail-formates/',mailformats,name="mailformats"),
    path('mail-content/<int:pk>',mailcontent,name="mailcontent")
]