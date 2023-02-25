from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Chat


# Create your views here.
@login_required()
def chats(request):
    chats = Chat.objects.all()
    return render(request, "chats/chats.html", {"chats": chats})

def chat(request, slug):
    chat =Chat.objects.get(slug=slug)
    return render(request,"chats/chat.html",{"chat":chat})

