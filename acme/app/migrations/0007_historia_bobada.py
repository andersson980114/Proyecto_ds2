# Generated by Django 3.1.6 on 2021-04-11 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20210408_0007'),
    ]

    operations = [
        migrations.AddField(
            model_name='historia',
            name='bobada',
            field=models.CharField(default=1, max_length=20, verbose_name='Raza'),
            preserve_default=False,
        ),
    ]