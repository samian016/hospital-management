# Generated by Django 3.0.3 on 2020-07-26 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicassist',
            name='username',
            field=models.TextField(unique=True),
        ),
    ]
