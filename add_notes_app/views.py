from django.shortcuts import render, redirect
from add_notes_app.models import Notes
from add_notes_app.forms import CreateNote, AddDescription

# Create your views here.
def index(request):
    noteForm = CreateNote()
    descForm = AddDescription()
    context={
        'noteForm': noteForm,
        'descForm': descForm,
        'all_notes': Notes.objects.all(),
    }
    return render(request, 'index.html',context)

def update_note(request):
    if request.method == "POST":
        desc = Notes.objects.get(id=request.POST['note_id'])
        desc.description = request.POST['description']
        desc.save()
        context = {
            'all_notes': Notes.objects.all()
            }  
    print('comment updated') 
    return render (request, 'notes.html', context)

def add_note(request):
    if request.method == 'POST':
        Notes.objects.create(subject=request.POST['subject'])
        context = {
            'all_notes': Notes.objects.all(),
        }
    # return redirect ('/')  
    print('Note posted') 
    return render (request, 'notes.html', context)

def delete(request, note_id):
    Notes.objects.get(id=note_id).delete()
    context = {
            'all_notes': Notes.objects.all(),
        }
    print('NOTE deleted') 
    return render (request, 'notes.html', context)
   


    