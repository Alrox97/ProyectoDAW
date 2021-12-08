from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Events
from .models import CustomUser

class SignUpForm(UserCreationForm):
    """
    Define la estructura de un formulario de login.
    """
    email = forms.CharField(max_length=400)
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email',)

class EventsForm(forms.ModelForm):
    """
    Define la estructura de un formulario para un empleado.
    """
    class Meta:
        model = Events
        fields = "__all__"