# Generated by Django 4.2.3 on 2023-08-31 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repositories', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='repository',
            name='repoImages',
        ),
        migrations.AddField(
            model_name='repository',
            name='background',
            field=models.ImageField(blank=True, null=True, upload_to='backgrounds/'),
        ),
        migrations.AddField(
            model_name='repository',
            name='RepoImages',
            field=models.ImageField(blank=True, null=True, upload_to='repository_images/'),
        ),
    ]
