# Generated by Django 5.0.6 on 2024-09-17 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0002_produto_preco_compra_produto_preco_venda_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='preco_compra',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='produto',
            name='preco_venda',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='produto',
            name='quantidade',
            field=models.FloatField(default=0),
        ),
    ]
