# Generated by Django 4.2.1 on 2023-09-05 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0003_category_shopitem_available_shopitem_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(choices=[('Tech', 'Technology'), ('Sci', 'Science'), ('Ent', 'Entertainment'), ('Other', 'Other')], max_length=150),
        ),
    ]
