# Generated by Django 5.0.1 on 2024-01-11 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_cad_user', '0002_usuarios_idade'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Usuarios',
            new_name='Usuario',
        ),
    ]
