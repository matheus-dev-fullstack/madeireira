# Generated by Django 5.1 on 2024-08-28 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('termo', '0006_alter_termo_dt_fim'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='equipamento',
            options={'ordering': ['equipamento'], 'verbose_name': 'Equipamento', 'verbose_name_plural': 'Equipamentos'},
        ),
    ]
