# Generated by Django 5.1.1 on 2024-11-26 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_alter_blog_published_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='published_at',
            new_name='publish_at',
        ),
    ]
