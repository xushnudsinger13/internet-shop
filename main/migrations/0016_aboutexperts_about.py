# Generated by Django 4.1 on 2022-08-06 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_remove_homeabout_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutexperts',
            name='about',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
