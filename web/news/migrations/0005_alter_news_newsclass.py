# Generated by Django 4.1.3 on 2022-12-31 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0004_rename_count_news_viewcounter"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="NewsClass",
            field=models.CharField(
                choices=[
                    ("Sport", "Sport"),
                    ("Health", "Health"),
                    ("Politics", "Politics"),
                    ("Economics", "Economics"),
                    ("Technology", "Technology"),
                ],
                max_length=100,
            ),
        ),
    ]