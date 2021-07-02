# Generated by Django 3.0.6 on 2020-08-10 19:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0006_patient_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='release_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='status',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]