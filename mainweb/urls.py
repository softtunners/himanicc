

from django.urls import path
from .views import *
urlpatterns = [
    path("", home, name="home"),
    path("contact", contact, name="contact"),
    path("about", about, name="about"),
    path('post/<int:pk>', blog, name="blog"),
    path("blogs", blogMain, name="blogs"),
    path("service", service, name="service"),
    path("scrapbook", scrapbook, name="scrapbook"),
    path("gallery/<int:pk>", Gallery, name="Gallery"),
    path('comment/<int:pk>',comment,name='comment'),
    path('subscribe/',subscribe,name='subscribe'),
    path('services',service,name='services'),
    path('blog-settings',blogsettingsview,name='blog-settings'),
    path('profiledetails', prashant, name='profiledetails'),
    path("like_post/<int:pk>", LikeView, name="like_post"),
    path("career", carrier, name="career"),
    path('career/<int:id>', careerApp, name="careerApp"),
    # path(r'career/skill/(?P<slug>[-a-zA-Z0-9_]+)\Z',skillsearch,name="skillsearch"),
        path('career/skill/<str:title>',skillsearch,name="skillsearch"),

    path(r'career/',skillsearch1,name="skillsearch1")

]
