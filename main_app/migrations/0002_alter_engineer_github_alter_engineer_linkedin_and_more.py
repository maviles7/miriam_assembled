# Generated by Django 5.1.1 on 2024-10-24 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engineer',
            name='github',
            field=models.URLField(max_length=500),
        ),
        migrations.AlterField(
            model_name='engineer',
            name='linkedin',
            field=models.URLField(max_length=500),
        ),
        migrations.AlterField(
            model_name='engineer',
            name='resume',
            field=models.URLField(max_length=500),
        ),
    ]
