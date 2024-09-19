from django.db import models

class Categoria(models.Model):
    titulo = models.CharField(max_length=40)
    
    def __str__(self):
        return self.titulo
    
class Produto(models.Model):
    nome = models.CharField(max_length=40)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    quantidade = models.FloatField(default=0)
    preco_compra = models.FloatField(default=0)   # o CORRETO SERIA preco_compra = models.BinaryField()
    preco_venda = models.FloatField(default=0)  
    
    def __str__(self):
        return self.nome
    
    def gerar_desconto(self, deconto):
        return self.preco_venda - ((self.preco_venda * deconto) /100)
    
    def lucro(self):
        lucro = self.preco_venda - self.preco_compra
        return (lucro * 100) / self.preco_compra
        # Vai retornar em porcentagem
        
class Imagem(models.Model):
    imagem = models.ImageField(upload_to='imagem_produto')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)