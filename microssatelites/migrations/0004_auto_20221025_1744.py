# Generated by Django 3.2.9 on 2022-10-25 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('microssatelites', '0003_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='fileGBK',
            field=models.BinaryField(verbose_name='File'),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='microssatelites.user')),
            ],
        ),
    ]
