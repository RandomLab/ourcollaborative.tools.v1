import datetime
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import (
    BooleanField,
    CharField,
    TextField,
    URLField,
    DateTimeField,
)

from django.template.defaultfilters import slugify

from embed_video.fields import EmbedVideoField
from django_resized import ResizedImageField

from autoslug import AutoSlugField


class Licence(models.Model):

    """
    A class to represent a licence.

    """

    title = CharField(max_length=250)

    description = TextField(blank=True)

    open = BooleanField(default=True)

    slug = AutoSlugField(populate_from="title")

    class Meta:
        """
        meta

        """

        ordering = ("title",)
        verbose_name = "licence"
        verbose_name_plural = "licences"

    def __str__(self) -> str:
        """return str representation of object"""
        return f"{self.title}"


class Notion(models.Model):

    """
    A class to represent a notion.

    """

    title = CharField(max_length=250)

    content = TextField(blank=True)

    publish = BooleanField(default=False)

    slug = AutoSlugField(populate_from="title")

    class Meta:

        """
        meta of the notion object.

        """

        ordering = ("title",)
        verbose_name = "notion"
        verbose_name_plural = "notions"

    def __str__(self) -> str:
        """return str representation of object"""
        return f"{self.title}"


class Article(models.Model):

    """
    A class to represent an article.

    """

    title = CharField(max_length=250)

    resume = TextField(blank=True)

    content = TextField(blank=True)

    # add a text in markdown as a file
    md_file = models.FileField(upload_to='article', blank=True, null=True)

    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True)

    date_pub = DateTimeField("Publication date", auto_now_add=True)

    slug = AutoSlugField(populate_from="title")

    publish = BooleanField(default=False)

    notion = models.ManyToManyField(
        Notion,
        blank=True,
    )

    licence = models.ForeignKey(
        "Licence", on_delete=models.SET_NULL, null=True, blank=True
    )

    class Meta:

        """
        meta of the article object.

        """

        ordering = ("title",)
        verbose_name = "article"
        verbose_name_plural = "articles"

    def save(self, *args, **kwargs):
        get_text = self.md_file.open().read()
        self.content = get_text
        super(Article, self).save(*args, **kwargs)

    def __str__(self) -> str:
        """return str representation of object"""
        return f"{self.title}"


def get_article_image_filename(instance, filename) -> str:
    """return str representation of object"""
    title = instance.article.title
    slug = slugify(title)
    return f"articles/{slug}/{filename}"


class ImageArticle(models.Model):

    """
    A class to represent a image for article.

    """

    legende = models.CharField(max_length=200)
    article = models.ForeignKey(Article, default=None, on_delete=CASCADE)
    image = ResizedImageField(force_format="WEBP", upload_to=get_article_image_filename)

    def __str__(self) -> str:
        """return str representation of object"""
        return f"{self.legende}"


def get_img(instance, filename) -> str:
    """return str representation of object"""
    title = instance.project.title
    slug = slugify(title)
    return f"projects/{slug}/{filename}"


class Project(models.Model):

    """
    A class to represent a project.

    """

    title = CharField(max_length=250)

    description = TextField(blank=True)

    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True)

    url = URLField(null=True, blank=True)

    thumbnail = ResizedImageField(size=[1580, 1000], crop=['middle', 'center'], force_format="WEBP", upload_to='thumb')

    date_pub = DateTimeField("Publication date", auto_now_add=True)

    date_creation = DateTimeField(
        "Creation date", default=datetime.datetime(2000, 1, 1), blank=True, null=True
    )

    no_date = BooleanField(default=False)

    slug = AutoSlugField(populate_from="title")

    video = EmbedVideoField(blank=True, null=True)

    publish = BooleanField(default=False)

    TIME_STATUS = (
        ("event", "Event"),
        ("continuous", "Continuous"),
    )

    temporality = CharField(
        max_length=15, choices=TIME_STATUS, blank=True, default="event"
    )

    USAGE_TYPE = (
        ("collaboration", "Collaboration"),
        ("cooperation", "Cooperation"),
        ("contribution", "Contribution"),
        ("participatory", "Participatory"),
    )

    usage = CharField(
        max_length=15, choices=USAGE_TYPE, blank=True, default="collaboration"
    )

    ENV_TYPE = (
        ("web", "Web"),
        ("desktop", "Desktop"),
        ("mobile", "Mobile"),
    )

    environment = CharField(
        max_length=15, choices=ENV_TYPE, blank=True, default="web"
    )

    licence = models.ForeignKey(
        "Licence", on_delete=models.SET_NULL, null=True, blank=True
    )

    notion = models.ManyToManyField(
        Notion,
        blank=True,
    )

    class Meta:

        """
        meta.

        """

        ordering = ("title",)
        verbose_name = "project"
        verbose_name_plural = "projects"

    def __str__(self) -> str:
        """return str representation of object"""
        return f"{self.title}"


class ImageProject(models.Model):

    """
    A class to represent a project image.

    """

    legende = models.CharField(max_length=200)
    project = models.ForeignKey(Project, default=None, on_delete=CASCADE)
    image = ResizedImageField(force_format="WEBP", upload_to=get_img)

    def __str__(self) -> str:
        """return str representation of object"""
        return f"{self.legende}"


class Author(models.Model):

    """
    A class to represent a author.

    """

    name = CharField(max_length=250)
    firstname = CharField(max_length=250, blank=True)

    group = BooleanField(default=False)

    bio = TextField(blank=True)

    url = URLField(null=True, blank=True)

    slug = AutoSlugField(populate_from="name", editable=True)

    PRONOUM_TYPE = (
        ("Her", "Her"),
        ("They", "They/Them"),
        ("Him", "Him"),
    )

    pronoun = CharField(max_length=10, choices=PRONOUM_TYPE, blank=True, default="Her")

    class Meta:
        """
        meta

        """

        ordering = (
            "name",
            "group",
        )
        verbose_name = "author"
        verbose_name_plural = "authors"

    def __str__(self) -> str:
        """return str representation of object"""
        if self.group:
            return f"{self.name}"
        else:
            return f"{self.firstname} {self.name}"
