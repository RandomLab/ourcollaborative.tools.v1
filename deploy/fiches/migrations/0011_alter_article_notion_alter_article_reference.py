# Generated by Django 4.1.5 on 2023-04-17 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fiches", "0010_reference_alter_article_notion_article_reference"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="notion",
            field=models.ManyToManyField(blank=True, to="fiches.notion"),
        ),
        migrations.AlterField(
            model_name="article",
            name="reference",
            field=models.ManyToManyField(blank=True, to="fiches.reference"),
        ),
    ]
