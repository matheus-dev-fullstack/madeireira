# Generated by Django 5.0.6 on 2024-10-21 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='senha',
            field=models.CharField(default='Usa@2024', max_length=100),
        ),
    ]
