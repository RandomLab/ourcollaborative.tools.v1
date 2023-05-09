# Generated by Django 4.1.5 on 2023-05-03 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fiches", "0018_rename_legende_imagearticle_legend_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="short_description",
            field=models.CharField(default="short", max_length=300),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="article",
            name="publish",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="author",
            name="pronoun",
            field=models.CharField(
                blank=True,
                choices=[
                    ("he/him", "He/Him"),
                    ("they/them", "They/Them"),
                    ("she/her", "She/Her"),
                ],
                default="Her",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="publish",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="project",
            name="usage",
            field=models.CharField(
                blank=True,
                choices=[
                    ("collaboration", "Collaboration"),
                    ("cooperation", "Cooperation"),
                    ("contribution", "Contribution"),
                    ("participation", "Participation"),
                ],
                default="collaboration",
                max_length=15,
            ),
        ),
    ]
