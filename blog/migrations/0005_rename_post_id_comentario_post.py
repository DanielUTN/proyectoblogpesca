# Generated by Django 4.1 on 2023-10-21 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comentario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='post_id',
            new_name='post',
        ),
    ]
