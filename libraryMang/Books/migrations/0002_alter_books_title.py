# Generated by Django 4.0.6 on 2022-07-13 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]