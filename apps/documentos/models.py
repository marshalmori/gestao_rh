from django.db import models

# Create your models here.
class Documento(models.Model):
    descricao = models.CharField(max_length=100)


    def __str__(self):
        return self.descricao

