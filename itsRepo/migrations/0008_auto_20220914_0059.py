# Generated by Django 3.2.5 on 2022-09-14 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itsRepo', '0007_auto_20220914_0049'),
    ]

    operations = [
        migrations.AddField(
            model_name='homework',
            name='final_stage',
            field=models.IntegerField(default=1, null=True),
        ),
        migrations.AddField(
            model_name='homework',
            name='initial_stage',
            field=models.IntegerField(default=1, null=True),
        ),
    ]