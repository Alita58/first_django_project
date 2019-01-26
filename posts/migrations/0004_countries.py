# Generated by Django 2.1.1 on 2018-12-08 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_delete_countries'),
    ]

    operations = [
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(choices=[('orange', 'Oranges'), ('cantaloupe', 'Cantaloupes'), ('mango', 'Mangoes'), ('honeydew', 'Honeydews')], max_length=50, null=True)),
            ],
            options={
                'verbose_name_plural': 'Countries',
            },
        ),
    ]