# Generated by Django 5.1.1 on 2024-11-27 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_alter_blog_publish_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='publish_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='publish at'),
        ),
    ]
