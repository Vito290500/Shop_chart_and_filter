# Generated by Django 4.2.1 on 2023-09-04 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopitem',
            name='ImageItem',
            field=models.ImageField(upload_to='images'),
        ),
    ]
