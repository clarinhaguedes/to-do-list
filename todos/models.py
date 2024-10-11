from django.db import models


# Create your models here.
class Todo(models.Model):
    task_name = models.CharField(verbose_name="Nome da Tarefa",
    max_length=100, null=False, blank=False)
    creation = models.DateTimeField(verbose_name="Data de criação",
    auto_now_add=True, null=False, blank=False)
    delivery = models.DateField(verbose_name="Data de entrega", 
    null=False, blank=False)
    finalization = models.DateField(null=True)

class Meta:
    ordering=["delivery"]
