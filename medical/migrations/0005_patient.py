# Generated by Django 3.0.6 on 2020-08-10 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('medical', '0004_delete_patient'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField()),
                ('second_name', models.TextField()),
                ('date_of_birth', models.DateField()),
                ('sex', models.TextField()),
                ('maritalS', models.TextField()),
                ('childrenN', models.IntegerField()),
                ('residence', models.TextField()),
                ('nationality', models.TextField()),
                ('occupation', models.TextField()),
                ('religion', models.TextField()),
                ('guardian_first_name', models.TextField()),
                ('guardian_second_name', models.TextField()),
                ('telephone', models.TextField()),
                ('disease', models.TextField()),
                ('ward', models.TextField()),
                ('bed', models.IntegerField()),
                ('care_note', models.TextField()),
                ('transfer_from', models.TextField()),
                ('pulse', models.IntegerField()),
                ('bloodP', models.IntegerField()),
                ('respiration', models.IntegerField()),
                ('tempe', models.IntegerField()),
                ('physical_con', models.TextField()),
            ],
        ),
    ]
