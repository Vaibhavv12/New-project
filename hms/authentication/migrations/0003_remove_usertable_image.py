# Generated by Django 4.0.4 on 2022-06-21 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_usertable_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usertable',
            name='image',
        ),
    ]