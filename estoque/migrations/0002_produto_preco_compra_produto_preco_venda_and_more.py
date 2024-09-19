# Generated by Django 5.0.6 on 2024-09-17 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='preco_compra',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='preco_venda',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='quantidade',
            field=models.FloatField(null=True),
        ),
    ]