# Generated by Django 4.1 on 2022-08-06 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_product_productservice'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='about/')),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
            ],
        ),
    ]