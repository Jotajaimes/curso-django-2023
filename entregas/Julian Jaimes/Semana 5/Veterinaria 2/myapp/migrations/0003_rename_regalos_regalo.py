# Generated by Django 4.2.7 on 2023-12-03 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_usuario_celular_alter_usuario_correo_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Regalos',
            new_name='Regalo',
        ),
    ]
