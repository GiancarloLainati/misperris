# Generated by Django 2.1.2 on 2018-10-29 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20181028_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rescatado',
            name='fotografia',
            field=models.ImageField(upload_to='media'),
        ),
    ]