# Generated by Django 2.0 on 2017-12-09 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('networkconnectivity', '0004_auto_20171209_1341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='networkdata',
            name='node',
        ),
    ]
