# Generated by Django 5.1.1 on 2025-01-04 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0004_alter_food_description_alter_food_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='price',
            field=models.FloatField(),
        ),
    ]
