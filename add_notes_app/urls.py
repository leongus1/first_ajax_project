from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_note', views.add_note, name='add_note'),
    path('update_note', views.update_note, name='update_note'),
    path('delete/<int:note_id>', views.delete),
]