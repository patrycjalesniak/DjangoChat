from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# model o nazwie Chat dziedziczy z model.Model z 2 polami name ktory jest CharField z max dlugoscia 255 i
# slug ktory jest polem Slug i ma parametr unique ustawiony na True

class Chat(models.Model):
    chat = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.chat


# Drugi model o nazwie Message z 4 polami:
# chat ktory jest kluczem obycm do modelu Chat i jego related_name jest ustawione na "message" i jest usuwany kaskadowo
# user ktory jest kluczem obycm do modelu User i jego related_name jest ustawione na "user" i jest usuwany kaskadowo
# content ktory bedzie zawartoscia naszej wiadomosci i bedzie Textem
# date_added ktory bedzie Date Timeem z auto_now_add ustawionym na prawde
# dodatkowo w meta danych nalezy podac ordering jest wzgledem "date_added"

class Message(models.Model):
    chat = models.ForeignKey(Chat, related_name='message', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    # https://www.geeksforgeeks.org/meta-class-in-models-django/
    # https://docs.djangoproject.com/en/4.1/ref/models/options/

    class Meta:
        ordering = ('date_added',)

    def __str__(self):
        return self.content

