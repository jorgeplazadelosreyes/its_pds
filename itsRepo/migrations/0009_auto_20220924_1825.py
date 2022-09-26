# Generated by Django 3.2.5 on 2022-09-24 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itsRepo', '0008_auto_20220914_0059'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='student',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='first_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='last_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]