# Generated by Django 4.0 on 2021-12-08 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dawi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='institucion',
            field=models.CharField(default=None, max_length=300),
            preserve_default=False,
        ),
    ]
