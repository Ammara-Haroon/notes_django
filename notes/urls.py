from django.urls import path

from . import views

urlpatterns = [
  path('',views.index,name='index'),
  path('delete_title/<int:id>',views.delete_title,name='delete_title'),
  path('add_title/',views.add_title,name="add_title"),
  path('update_title/<int:id>',views.update_title,name="update_title"),
  path('delete_note/<int:id>',views.delete_note,name='delete_note'),
  path('add_note/<int:id>',views.add_note,name="add_note"),
  path('update_note/<int:id>',views.update_note,name="update_note"),

]