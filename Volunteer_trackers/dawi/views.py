from django.shortcuts import render
from django.db.models.manager import EmptyManager
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.views.generic.base import TemplateView
from .forms import SignUpForm, EventsForm
from .models import Events
from django.views.generic import ListView, DetailView
from datetime import datetime

def searchEvents(request):
    if request.method=="POST":
        searched = request.POST('searched')
        events = Events.objects.filter(name__contains=searched)

        return render(request, 'volunteers/searchEvents.html',
        {'searched':searched,
         'events':events})
    else:
        return render(request, 'volunteers/searchEvents.html',{})

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

class IndexView(ListView):
    """
    Visualiza la lista de eventos :model:`authen.Events`.
    **Context**
    ``Events``
        Una instancia de :model:`authen.Events`.
    **Template:**
    :template:`volunteers/myprofileVolun.html`
    """
    template_name = 'volunteers/myprofileVolun.html'
    context_object_name = 'events_list'

    def get_queryset(self):
        return Events.objects.all()


def create(request):
    """
    despliega un formulario para capturar los datos de un empleado.
    **Template:**
    :template:`volunteers/myprofileVolun.html`
    """
    if request.method == 'POST':
        form = EventsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/myprofileVolun')
    form = Events()
    return redirect('/myprofileVolun')


def update(request, id):
    """
    Despliega un formulario para actualizar los datos de un determinado empleado.
    **Template:**
    :template:`volunteers/myprofileVolun.html`
    """
    events = Events.objects.get(id=id)
    form = EventsForm(request.POST, instance=events)
    if form.is_valid():
        form.save()
        return redirect("/myprofileVolun")


def delete(request, id):
    """
    Despliega un modal de confirmación para eliminar un empleado en concreto.
    **Template:**
    :template:`volunteers/myprofileVolun.html`
    """
    events = Events.objects.get(id=id)
    events.delete()
    return redirect("/myprofileVolun")


def deletelist(request):
    """
    Despliega un modal de confirmación para eliminar varios eventos en concreto.
    **Template:**
    :template:`volunteers/myprofileVolun.html`
    """
    lista = dict(request.POST)
    for element in lista['idCollection[]']:
        events = Events.objects.get(id=element)
        events.delete()

class IndexView(ListView):
   
    template_name = 'institutions/myprofileInst.html'
    context_object_name = 'events_list'

    def get_queryset(self):
        return Events.objects.all()


def create(request):
    """
    despliega un formulario para capturar los datos de un empleado.
    **Template:**
    :template:`institutions/myprofileInst.html`
    """
    if request.method == 'POST':
        form = EventsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/myprofileInst')
    form = Events()
    return redirect('/myprofileInst')


def update(request, id):
    """
    Despliega un formulario para actualizar los datos de un determinado empleado.
    **Template:**
    :template:`institutions/myprofileInst.html`
    """
    events = Events.objects.get(id=id)
    form = EventsForm(request.POST, instance=events)
    if form.is_valid():
        form.save()
        return redirect("/myprofileInst")


def delete(request, id):
    """
    Despliega un modal de confirmación para eliminar un empleado en concreto.
    **Template:**
    :template:`institutions/myprofileInst.html`
    """
    events = Events.objects.get(id=id)
    events.delete()
    return redirect("/myprofileInst")


def deletelist(request):
    """
    Despliega un modal de confirmación para eliminar varios eventos en concreto.
    **Template:**
    :template:`institutions/myprofileInst.html`
    """
    lista = dict(request.POST)
    for element in lista['idCollection[]']:
        events = Events.objects.get(id=element)
        events.delete()