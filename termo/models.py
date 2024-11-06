from datetime import datetime
from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    cracha = models.CharField(max_length=12)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['nome']

class Equipamento(models.Model):
    equipamento =  models.CharField(max_length=40, blank=True)
    marca =  models.CharField(max_length=40)
    modelo =  models.CharField(max_length=40)
    maq =  models.CharField(max_length=20, blank=True)
    patrimonio =  models.CharField(max_length=20, blank=True)
    
    def __str__(self):
        equipamento = str(self.equipamento) if self.equipamento else ''
        maq = str(self.maq) if self.maq else ''
        marca = str(self.marca) if self.marca else ''
        modelo = str(self.modelo) if self.modelo else ''
        patrimonio = str(self.patrimonio) if self.patrimonio else ''
        
        parts = [equipamento, marca, maq, modelo, patrimonio]
        
        # return equipamento
        return "{} - {} {} - {}".format(self.equipamento , self.modelo,self.maq, self.patrimonio)
    
    class Meta:
        verbose_name = 'Equipamento'
        verbose_name_plural = 'Equipamentos'
        ordering = ['equipamento']
    

class Tipo(models.TextChoices):
    PERMANENTE = 'Permanente', 'Permanente'
    EMPRESTIMO = 'Emprestimo', 'Empréstimo'
    
class Termo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE, default=None)
    tipo = models.CharField(max_length=100, choices=Tipo.choices)
    dt_inicio = models.DateField()
    dt_fim = models.DateField(null=True, blank=True)
    descricao = models.CharField(max_length=244, blank=True)
    
    def __str__(self):
        equipamento = str(self.equipamento) if self.equipamento else ''
        usuario = str(self.usuario) if self.usuario else ''
        dt_inicio = self.dt_inicio.strftime('%d/%m/%Y') if self.dt_inicio else ''

        parts = [dt_inicio ,equipamento, usuario]

    
        return ' - '.join(part for part in parts if part)


    
    class Meta:
        verbose_name = 'Termo'
        verbose_name_plural = 'Termos'
        ordering = ['dt_inicio']

# Usuário (nome, crachá)
# Equipamento (marca, modelo, MAQ, Patrimônio)
# Tipo (Permanente ou Emprestimo)
# Termo (Usuário, Equipamento, Tipo, data, data fim?)