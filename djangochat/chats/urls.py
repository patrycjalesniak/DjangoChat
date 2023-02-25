from django.urls import path
from .views import chats, chat



urlpatterns = [
    path("", chats, name="chats"),
    path("<slug:slug>/", chat, name="chat"),
]