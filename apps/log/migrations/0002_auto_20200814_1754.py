# Generated by Django 2.2.7 on 2020-08-14 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formallogin',
            name='confirmation',
            field=models.FileField(upload_to='confirmation/%Y%m%d'),
        ),
        migrations.AlterModelTable(
            name='formallogin',
            table='FormalLogin',
        ),
    ]
