from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="blogHome"),
    path("blogpost/<int:id>", views.blogpost, name="blogHome"),
    path("contact/", views.contact, name="ContactUs"),
    path("about/", views.about, name="About")
]
