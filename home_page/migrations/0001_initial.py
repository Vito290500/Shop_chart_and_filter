# Generated by Django 4.2.1 on 2023-09-04 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShopItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NameItem', models.CharField(max_length=150)),
                ('ImageItem', models.ImageField(upload_to='')),
                ('DataItem', models.DateField()),
                ('PriceItem', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('TagItem', models.CharField(max_length=150)),
            ],
        ),
    ]
