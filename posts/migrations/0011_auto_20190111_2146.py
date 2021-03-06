# Generated by Django 2.1.1 on 2019-01-11 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_destination'),
    ]

    operations = [
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_key', models.CharField(max_length=100)),
                ('text', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Texts',
            },
        ),
        migrations.AlterField(
            model_name='destination',
            name='destination',
            field=models.CharField(max_length=200),
        ),
    ]
