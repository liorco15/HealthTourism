# Generated by Django 3.1.3 on 2020-11-29 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20201129_1659'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=30)),
                ('phone_number', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('reason_for_referral', models.CharField(max_length=250)),
            ],
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
    ]
