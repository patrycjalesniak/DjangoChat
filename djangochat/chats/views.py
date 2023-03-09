from django.shortcuts import render
from .models import Chat, Message
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def chats(request):
    chats = Chat.objects.all()
    return render(request, 'chats/chats.html', {'chats': chats})


@login_required
def chat(request, slug):
    chat = Chat.objects.get(slug=slug)
    messages = Message.objects.filter(chat=chat)[:25]
    return render(request, 'chats/chat.html', {'chat': chat, 'messages': messages})
