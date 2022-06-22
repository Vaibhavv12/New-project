# Generated by Django 4.0.4 on 2022-06-21 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_remove_usertable_entry_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertable',
            name='user_DOB',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usertable',
            name='user_LastSemScore',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usertable',
            name='user_address',
            field=models.CharField(default=1, max_length=45),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usertable',
            name='user_name',
            field=models.CharField(default=1, max_length=45),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usertable',
            name='user_presentyear',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]
