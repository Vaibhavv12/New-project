# Generated by Django 4.0.4 on 2022-06-21 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_remove_usertable_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usertable',
            name='entry_date',
        ),
    ]
