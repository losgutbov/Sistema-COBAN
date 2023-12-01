from django.db import models

# Create your models here.
class Consulta(models.Model):
    nome_consulta = models.CharField("Nome da Consulta", max_length=45) 
    consulta_sql = models.TextField("Consulta SQL")
    data_criacao = models.DateTimeField("Data de Criação", auto_now=True)
    data_modificacao = models.DateTimeField("Data de Modificação", null=True)
    ativo = models.BooleanField("Consulta Ativa", default=True)
    view_vinculada = models.CharField("View Vinculada", max_length=45, null=True, blank=True)
    contagem_uso = models.SmallIntegerField("Contagem de Uso da Consulta", null=True, blank=True)

    def __str__(self) -> str:
        return self.nome_consulta
    
    def uso_total(self):
        return self.contagem_uso

