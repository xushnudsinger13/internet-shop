# Generated by Django 4.1 on 2022-08-06 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_services'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='smalltitle',
        ),
    ]