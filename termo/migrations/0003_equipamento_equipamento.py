# Generated by Django 5.0.7 on 2024-07-24 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('termo', '0002_alter_equipamento_options_alter_termo_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipamento',
            name='equipamento',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
