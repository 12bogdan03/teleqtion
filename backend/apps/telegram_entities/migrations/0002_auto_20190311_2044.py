# Generated by Django 2.1.5 on 2019-03-11 20:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('telegram_entities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegramgroup',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='telegram_groups', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='telegramcontact',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='telegram_contacts', to='telegram_entities.TelegramGroup'),
        ),
        migrations.AddField(
            model_name='telegramcontact',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='telegram_contacts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to=settings.AUTH_USER_MODEL),
        ),
    ]