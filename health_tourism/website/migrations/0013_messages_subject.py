# Generated by Django 3.1.3 on 2021-01-08 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_event_messages'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='subject',
            field=models.CharField(default='SOME STRING', max_length=20),
        ),
    ]
