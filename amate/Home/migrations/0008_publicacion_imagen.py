# Generated by Django 4.0.4 on 2022-06-27 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0007_remove_publicacion_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='imagen',
            field=models.ImageField(default='', upload_to='home'),
            preserve_default=False,
        ),
    ]