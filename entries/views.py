from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render

from .forms import DiaryEntryForm
from .models import DiaryEntry


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('all_entries')
    else:
        form = UserCreationForm()
    return render(request, 'auth/registration.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('all_entries')
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('user_login')


@login_required
def all_entries(request):
    entries = DiaryEntry.objects.filter(user=request.user)
    return render(request, 'all_entries.html', {'entries': entries})

@login_required
def view_entry(request, entry_id):
    entry = get_object_or_404(DiaryEntry, id=entry_id, user=request.user)
    return render(request, 'view_entry.html', {'entry': entry})

@login_required
def add_or_modify_entry(request, entry_id=None):
    if entry_id:
        entry = get_object_or_404(DiaryEntry, id=entry_id, user=request.user)
    else:
        entry = None
    
    if request.method == 'POST':
        form = DiaryEntryForm(request.POST, instance=entry)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect('all_entries')
    else:
        form = DiaryEntryForm(instance=entry)
    
    return render(request, 'add_modify_entry.html', {'form': form})
