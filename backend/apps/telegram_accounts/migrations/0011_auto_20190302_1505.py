# Generated by Django 2.1.5 on 2019-03-02 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_accounts', '0010_auto_20190209_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telegramaccount',
            name='active',
            field=models.BooleanField(default=False, help_text='Banned or not banned.', verbose_name='Active'),
        ),
    ]
