# Generated by Django 4.2.7 on 2023-11-15 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='altura',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AddField(
            model_name='usuarios',
            name='peso',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=3),
        ),
    ]
