# Generated by Django 4.1 on 2022-08-06 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='about',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]