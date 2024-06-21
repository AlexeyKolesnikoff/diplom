# Generated by Django 5.0.6 on 2024-06-19 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_news_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField(blank=True)),
                ('last_name', models.TextField(blank=True)),
                ('age', models.CharField(db_index=True, max_length=3)),
                ('sport', models.TextField(blank=True)),
                ('phone', models.CharField(db_index=True, max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='news',
            name='slug',
        ),
    ]