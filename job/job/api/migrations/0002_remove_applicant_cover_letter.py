# Generated by Django 3.2.4 on 2022-09-22 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicant',
            name='cover_letter',
        ),
    ]
