# Generated by Django 3.1.5 on 2021-01-09 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_messages_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(default='SOME STRING', max_length=20)),
                ('full_name', models.CharField(max_length=20)),
                ('passport_num', models.CharField(max_length=20)),
                ('request', models.CharField(max_length=250)),
            ],
        ),
    ]
