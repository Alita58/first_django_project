# Generated by Django 2.1.1 on 2018-12-09 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20181209_0056'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(choices=[('Germany', 'Germany'), ('Poland', 'Poland')], max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Destinations',
            },
        ),
    ]
