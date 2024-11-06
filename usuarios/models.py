from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password



class Users(AbstractUser):
    username = models.CharField(max_length=100, unique=True, blank=True, null=True)
    password = models.CharField(max_length=100)
    choices_cargo =(('V', 'Vendedor'), ('G', 'Gerente'))
    cargo = models.CharField(max_length=1, choices=choices_cargo)
    
    def save(self, *args, **kwargs):
        if not self.password.startswith('pbkdf2_'):  # Verifica se já é um hash
            self.password = make_password(self.password)  # Gera o hash da senha
        super().save(*args, **kwargs)
        
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
    
    def __str__(self):
        return self.username 
