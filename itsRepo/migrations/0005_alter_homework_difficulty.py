# Generated by Django 4.1.1 on 2022-09-13 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itsRepo', '0004_rename_description_homework_statement_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='difficulty',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
