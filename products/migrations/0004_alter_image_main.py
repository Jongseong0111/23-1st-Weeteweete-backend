# Generated by Django 3.2.6 on 2021-08-05 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_image_main'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='main',
            field=models.BooleanField(default=False),
        ),
    ]
