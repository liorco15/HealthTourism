# Generated by Django 3.1.3 on 2021-01-10 00:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0013_messages_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documentation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('reason_why', models.CharField(max_length=250)),
                ('meeting', models.CharField(max_length=250)),
                ('diagnosis', models.CharField(max_length=250)),
            ],
        ),
        migrations.AlterField(
            model_name='messages',
            name='subject',
            field=models.CharField(default='SomeString', max_length=20),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=20)),
                ('last_name', models.CharField(blank=True, max_length=20)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=10)),
                ('email', models.EmailField(blank=True, max_length=30)),
                ('phone_number', models.CharField(blank=True, max_length=50)),
                ('country', models.CharField(blank=True, max_length=50)),
                ('reason_why', models.CharField(blank=True, default='a', max_length=50)),
                ('meeting', models.CharField(blank=True, default='a', max_length=50)),
                ('diagnosis', models.CharField(blank=True, default='a', max_length=50)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
