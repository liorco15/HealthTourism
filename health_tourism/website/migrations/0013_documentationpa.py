# Generated by Django 3.0.8 on 2021-01-08 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_event_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentationPA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'event',
                'verbose_name_plural': 'events',
                'ordering': ('-created_at',),
                'default_related_name': 'events',
            },
        ),
    ]
