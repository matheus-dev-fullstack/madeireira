# Generated by Django 5.1 on 2024-08-28 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('termo', '0004_termo_descricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipamento',
            name='maq',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='patrimonio',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='termo',
            name='dt_fim',
            field=models.DateField(blank=True),
        ),
    ]