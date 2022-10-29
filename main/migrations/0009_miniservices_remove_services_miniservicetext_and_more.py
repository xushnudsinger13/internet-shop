# Generated by Django 4.1 on 2022-08-06 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_services_smalltitle'),
    ]

    operations = [
        migrations.CreateModel(
            name='MiniServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('miniservicetitle', models.CharField(max_length=255)),
                ('miniservicetext', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='services',
            name='miniservicetext',
        ),
        migrations.RemoveField(
            model_name='services',
            name='miniservicetitle',
        ),
    ]