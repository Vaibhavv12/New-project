# Generated by Django 4.0.4 on 2022-06-09 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='image',
            field=models.ImageField(default='', upload_to='home/images'),
        ),
    ]