# Generated by Django 3.0 on 2021-02-08 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0012_auto_20210208_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='data_form',
            name='photograph',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='data_form',
            name='why_study',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]