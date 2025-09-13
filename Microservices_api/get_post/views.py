from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Note

# Create your views here.

@api_view(['GET', 'POST'])
def notes(request):
    if request.method == 'POST':
        title = request.data.get('title')
        content = request.data.get('content')
        note = Note.objects.create(title=title, content=content)
        return Response({"id": note.id, "message": "Note created successfully"})

    elif request.method == 'GET':
        notes = Note.objects.all()
        data = [{"id": n.id, "title": n.title, "content": n.content} for n in notes]
        return Response(data)
