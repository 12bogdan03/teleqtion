# Generated by Django 2.1.5 on 2019-02-09 17:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_entities', '0005_auto_20190209_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
