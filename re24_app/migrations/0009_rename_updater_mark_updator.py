# Generated by Django 3.2.12 on 2022-10-04 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('re24_app', '0008_auto_20221004_1503'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mark',
            old_name='updater',
            new_name='updator',
        ),
    ]
