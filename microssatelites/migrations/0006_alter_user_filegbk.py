# Generated by Django 3.2.9 on 2022-10-25 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microssatelites', '0005_remove_project_headline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='fileGBK',
            field=models.BinaryField(blank=True, null=True, verbose_name='File'),
        ),
    ]
