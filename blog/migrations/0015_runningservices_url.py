# Generated by Django 3.1 on 2022-01-21 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_runningservices'),
    ]

    operations = [
        migrations.AddField(
            model_name='runningservices',
            name='url',
            field=models.URLField(null=True),
        ),
    ]