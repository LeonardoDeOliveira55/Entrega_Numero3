# Generated by Django 4.2.3 on 2023-09-12 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppStark', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contratacion',
            name='servicio',
        ),
    ]
