from django.db import models
from django.contrib.auth.models import User
from apps.departamentos.models import Departamento

# Create your models here.

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    #user = models.OneToOneField(User, on_delete=models.PROTECT)
    departamentos = models.ManyToManyField(Departamento)


    def __str__(self):
        return self.nome