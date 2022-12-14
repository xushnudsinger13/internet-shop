# Generated by Django 4.1 on 2022-08-06 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_home'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeAboutService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('text', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='HomeAbout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('minititle', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('service', models.ManyToManyField(to='main.homeaboutservice')),
            ],
        ),
    ]
