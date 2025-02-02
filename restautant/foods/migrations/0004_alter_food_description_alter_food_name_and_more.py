# Generated by Django 5.1.1 on 2025-01-04 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0003_alter_food_type_food'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='description',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='food',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='food',
            name='photo',
            field=models.ImageField(upload_to='foods/'),
        ),
        migrations.AlterField(
            model_name='food',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='food',
            name='pub_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='rate',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='food',
            name='time',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='food',
            name='type_food',
            field=models.CharField(choices=[('drinks', 'drinks'), ('dinner', 'dinner'), ('lunch', 'lunch')], max_length=10),
        ),
    ]
