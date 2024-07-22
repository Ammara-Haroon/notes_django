import json
from django.http import HttpResponse
from django.shortcuts import redirect, render

from notes.forms import NoteForm, TitleForm
from notes.models import Note, Title

def index(request):
  form= TitleForm()
  note_form = NoteForm()
  titles = Title.objects.get_queryset()
  colors = ["#ff8039","#55bedb","#61d17b","#f7de36","#ef719b","#b460db"]
  context = {"title_form":form,"titles":titles,'note_form':note_form,'colors':colors}
  return render(request,'index.html',context)


def add_title(request):
  form = TitleForm(request.POST)
  if form.is_valid():
    form.save()
  return redirect('index')

def change_title(request,id):
  title = Title.objects.get(pk = id)
  print(request.POST.keys())
  if "edit" in request.POST.keys():
    title.description = request.POST.get("title_input").strip().title()
    title.save()
  
  if "delete" in request.POST.keys():
    title.delete()
  
  return redirect('index')
  

def add_note(request,id):
  form = NoteForm(request.POST)
  if form.is_valid():
    note = Note()
    note.title = Title.objects.get(pk=id)
    note.description = form.data.get("description").strip().lower()
    note.save()
  return redirect('index')

def change_note(request,id):
  print(request.POST)
  note = Note.objects.get(pk = id)
  if "edit" in request.POST.keys():
    note.description = request.POST.get("note_input").strip().lower()
    note.save()
  
  if "delete" in request.POST.keys():
    note.delete()
  
  return redirect('index')
  


