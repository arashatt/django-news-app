# Generated by Django 4.1.3 on 2022-12-23 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="news",
            name="NewsBody",
            field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="news",
            name="Count",
            field=models.IntegerField(default=0),
        ),
    ]
