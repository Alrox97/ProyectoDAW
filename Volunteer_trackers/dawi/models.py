from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    """
    Describe datos adicionales para guardar usuarios.
    """
    email = models.CharField(max_length=300, blank=False)

class Events(models.Model):
    """
    Describe los datos de un empleado.
    """
    name = models.CharField(max_length=100, default='DEFAULT VALUE')
    email = models.CharField(max_length=100, default='DEFAULT VALUE')
    address = models.CharField(max_length=100, default='DEFAULT VALUE')
    phone_num= models.CharField(max_length=100, default='DEFAULT VALUE')
    class Meta:
        db_table = 'events'