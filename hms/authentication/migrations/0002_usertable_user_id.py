# Generated by Django 4.0.4 on 2022-06-21 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertable',
            name='user_id',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
