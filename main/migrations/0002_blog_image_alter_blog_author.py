# Generated by Django 5.1.6 on 2025-03-03 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
