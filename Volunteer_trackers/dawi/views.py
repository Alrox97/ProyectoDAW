from django.shortcuts import render
from django.db.models.manager import EmptyManager
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.views.generic.base import TemplateView
from .forms import SignUpForm, EventsForm
from .models import Events
from django.views.generic import ListView, DetailView
from datetime import datetime
    

def home(request):
    """
    Renderiza una pantalla de inicio.
    **Template:**
    :template:`home/home.html`
    """
    return render(request, 'home/home.html')


def signup(request):
    """
    Despliega el login de usuario.
    **Template:**
    :template:`authen/signup.html`
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        try:
            if form.is_valid():
                user = form.save()
                user.save()
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=user.username,
                                    password=raw_password)
                login(request, user)
                return redirect('/login')
        except:
            return redirect('/login')
    else:
        form = SignUpForm()
    return render(request, 'authen/signup.html', {'form': form})
