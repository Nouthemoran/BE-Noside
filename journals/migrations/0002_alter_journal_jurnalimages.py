# Generated by Django 4.2.3 on 2023-09-05 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='jurnalImages',
            field=models.ImageField(blank=True, null=True, upload_to='journal_images/'),
        ),
    ]
