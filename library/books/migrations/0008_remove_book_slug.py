# Generated by Django 3.0.7 on 2020-07-03 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_book_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='slug',
        ),
    ]
