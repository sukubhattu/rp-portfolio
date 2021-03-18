from django.urls import path
from django.urls.resolvers import URLPattern

from .views import home, single_user


urlpatterns = [
    path("", view=home, name="index"),
    path("single/", view=single_user, name="single"),
]
