# Generated by Django 5.0.7 on 2024-07-17 13:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=40)),
                ('modelo', models.CharField(max_length=40)),
                ('maq', models.CharField(max_length=20)),
                ('patrimonio', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cracha', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Termo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('Permanente', 'Permanente'), ('Emprestimo', 'Empréstimo')], max_length=100)),
                ('dt_inicio', models.DateTimeField()),
                ('dt_fim', models.DateTimeField()),
                ('equipamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='termo.equipamento')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='termo.usuario')),
            ],
        ),
    ]
