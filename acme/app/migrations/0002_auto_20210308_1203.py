# Generated by Django 3.1.6 on 2021-03-08 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='Activo',
        ),
        migrations.AddField(
            model_name='usuario',
            name='Estado',
            field=models.IntegerField(choices=[[1, 'Activo'], [2, 'Inactivo']], default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='Cargo',
            field=models.IntegerField(choices=[[1, 'Veterinario'], [2, 'Recepcionista']]),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='Correo',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='Direccion',
            field=models.CharField(max_length=50),
        ),
    ]
