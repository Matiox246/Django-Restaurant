# Generated by Django 5.1.1 on 2024-11-25 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_blog_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='update_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
