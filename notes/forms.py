from django import forms
from .models import Note, Title
 
 
class TitleForm(forms.ModelForm):
    class Meta:
        model = Title
        fields = ['description',]
        labels={'description':''}

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['description']
        labels={'description':''}