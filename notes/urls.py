from django.urls import path

from . import views

urlpatterns = [
  path('',views.index,name='index'),
  path('change_title/<int:id>',views.change_title,name='change_title'),
  path('add_title/',views.add_title,name="add_title"),
  path('change_note/<int:id>',views.change_note,name='change_note'),
  path('add_note/<int:id>',views.add_note,name="add_note"),
  
]