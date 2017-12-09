# Generated by Django 2.0 on 2017-12-09 17:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('networkconnectivity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='networkdata',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='networknode',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='networknode',
            name='location_of_pi',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='networknode',
            name='mac_address',
            field=models.CharField(max_length=17),
        ),
    ]
