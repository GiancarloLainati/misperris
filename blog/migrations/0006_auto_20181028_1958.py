# Generated by Django 2.1.2 on 2018-10-28 22:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_rescatado_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='rescatado',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='rescatado',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]