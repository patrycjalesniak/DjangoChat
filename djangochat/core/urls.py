from django.urls import path
from .views import frontpage, signup


urlpatterns = [
    path("", frontpage, name="frontpage"),
#     path("login/" , WIDOK, name="login"),
    path("signup/", signup, name="signup"),
#     path("logout/",WIDOK,name="logout"),
]