# Generated by Django 4.1.3 on 2023-10-23 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20231022_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='email',
            field=models.EmailField(max_length=150, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]