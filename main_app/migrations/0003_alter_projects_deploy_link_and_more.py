# Generated by Django 5.1.1 on 2024-10-24 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_engineer_github_alter_engineer_linkedin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='deploy_link',
            field=models.URLField(max_length=500),
        ),
        migrations.AlterField(
            model_name='projects',
            name='github_link',
            field=models.URLField(max_length=500),
        ),
    ]
