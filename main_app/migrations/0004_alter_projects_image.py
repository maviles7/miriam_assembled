# Generated by Django 5.1.1 on 2024-10-24 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_projects_deploy_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='image',
            field=models.URLField(max_length=500),
        ),
    ]
