# Generated by Django 3.2.12 on 2022-10-03 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('re24_app', '0002_auto_20221003_1117'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mark',
            old_name='Id',
            new_name='student_id',
        ),
    ]