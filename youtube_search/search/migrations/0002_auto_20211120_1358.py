# Generated by Django 3.2.9 on 2021-11-20 10:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultmodel',
            name='pubdate',
            field=models.CharField(default=django.utils.timezone.now, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resultmodel',
            name='thumb',
            field=models.CharField(default='https', max_length=1000),
            preserve_default=False,
        ),
    ]
