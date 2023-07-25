from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    ultimo_nome = models.CharField(max_length= 50)
    data_nascimento = models.DateField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    
    def __str__(self):
        return self.nome

