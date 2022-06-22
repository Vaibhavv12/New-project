# Generated by Django 4.0.4 on 2022-06-21 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_student', models.BooleanField()),
                ('is_verified', models.BooleanField()),
                ('entry_date', models.DateField()),
                ('image', models.ImageField(default='', upload_to='home/images')),
            ],
        ),
    ]