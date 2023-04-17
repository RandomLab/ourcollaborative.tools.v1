# Generated by Django 4.1.5 on 2023-04-17 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fiches", "0009_alter_project_temporality_alter_project_usage"),
    ]

    operations = [
        migrations.CreateModel(
            name="Reference",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=250)),
                ("author", models.CharField(max_length=250)),
                ("editor", models.CharField(max_length=250)),
                ("sub_title", models.CharField(max_length=250)),
                (
                    "date_pub",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Publication date"
                    ),
                ),
                ("pages", models.CharField(max_length=50)),
                ("url", models.URLField(blank=True, null=True)),
                (
                    "media_type",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("book", "Book"),
                            ("article", "Article"),
                            ("thesis", "Thesis"),
                            ("video", "Video"),
                            ("website", "Website"),
                            ("video_game", "Video game"),
                            ("podcast", "Podcast"),
                        ],
                        default="book",
                        max_length=15,
                    ),
                ),
            ],
            options={
                "verbose_name": "reference",
                "verbose_name_plural": "references",
                "ordering": ("title",),
            },
        ),
        migrations.AlterField(
            model_name="article",
            name="notion",
            field=models.ManyToManyField(blank=True, null=True, to="fiches.notion"),
        ),
        migrations.AddField(
            model_name="article",
            name="reference",
            field=models.ManyToManyField(blank=True, null=True, to="fiches.reference"),
        ),
    ]
