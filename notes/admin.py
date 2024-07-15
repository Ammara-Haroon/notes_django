from django.contrib import admin

from notes.models import Note
from notes.models import Title

# Register your models here.
admin.site.register(Note)
admin.site.register(Title)
