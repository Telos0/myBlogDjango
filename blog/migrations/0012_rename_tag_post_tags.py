# Generated by Django 4.0.1 on 2022-01-18 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_tag_post_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tag',
            new_name='tags',
        ),
    ]
