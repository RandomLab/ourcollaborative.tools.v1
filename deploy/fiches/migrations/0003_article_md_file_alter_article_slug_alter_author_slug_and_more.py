# Generated by Django 4.1.5 on 2023-02-16 16:43

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fiches", "0002_alter_licence_options_rename_name_licence_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="md_file",
            field=models.FileField(blank=True, null=True, upload_to=None),
        ),
        migrations.AlterField(
            model_name="article",
            name="slug",
            field=autoslug.fields.AutoSlugField(editable=False, populate_from="title"),
        ),
        migrations.AlterField(
            model_name="author",
            name="slug",
            field=autoslug.fields.AutoSlugField(editable=False, populate_from="name"),
        ),
        migrations.AlterField(
            model_name="licence",
            name="slug",
            field=autoslug.fields.AutoSlugField(editable=False, populate_from="title"),
        ),
        migrations.AlterField(
            model_name="notion",
            name="slug",
            field=autoslug.fields.AutoSlugField(editable=False, populate_from="title"),
        ),
        migrations.AlterField(
            model_name="project",
            name="slug",
            field=autoslug.fields.AutoSlugField(editable=False, populate_from="title"),
        ),
    ]
