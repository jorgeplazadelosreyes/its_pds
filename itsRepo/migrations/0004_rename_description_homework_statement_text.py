# Generated by Django 3.2.5 on 2022-09-13 02:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('itsRepo', '0003_auto_20220912_1941'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homework',
            old_name='description',
            new_name='statement_text',
        ),
    ]
