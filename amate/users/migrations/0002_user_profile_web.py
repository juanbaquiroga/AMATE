# Generated by Django 4.0.4 on 2022-07-04 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='web',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
