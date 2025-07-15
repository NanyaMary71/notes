from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect
from .models import Note
from .forms import NoteForm


def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    note.delete()
    return redirect('home')

def edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NoteForm(instance=note)
    return render(request, 'edit_note.html', {'form': form, 'note': note})




def home(request):
    notes = Note.objects.all()

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NoteForm()

    return render(request, 'home.html', {'notes': notes, 'form': form})


# Create your views here.
