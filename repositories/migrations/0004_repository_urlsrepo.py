# Generated by Django 4.2.3 on 2023-09-05 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repositories', '0003_rename_repoimages_repository_repoimages'),
    ]

    operations = [
        migrations.AddField(
            model_name='repository',
            name='urlsRepo',
            field=models.URLField(blank=True, null=True),
        ),
    ]
