# Generated by Django 5.0.6 on 2024-06-19 19:40

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_remove_news_content_remove_news_pub_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, help_text='Введите дату события', null=True, verbose_name='Дата события'),
        ),
    ]
