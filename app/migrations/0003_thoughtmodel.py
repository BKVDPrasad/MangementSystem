# Generated by Django 3.0.3 on 2020-05-16 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_newusermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThoughtModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usernaem', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('contno', models.IntegerField()),
            ],
        ),
    ]