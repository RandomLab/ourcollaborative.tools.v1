from django.contrib import admin
from django.db import models
from embed_video.admin import AdminVideoMixin
from .widgets import DateTimePicker
from .models import (
    Project,
    Author,
    Licence,
    Notion,
    Article,
    Reference,
    ImageArticle,
    ImageProject,
)


@admin.register(Reference)
class Reference(admin.ModelAdmin):
    """
    A class to represent a reference.
    """

    list_display = ["title", "publish", "date_pub"]
    formfield_overrides = {
        models.DateField: {"widget": DateTimePicker}
    }
    # def date_pub(self, obj):
    #     return obj.date.strftime('%b, %Y')
    #
    # date_pub.admin_order_field = 'date'
    # date_pub.short_description = 'Date'


@admin.register(Notion)
class NotionAdmin(admin.ModelAdmin):
    """
    A class to represent an article.
    """

    list_display = ["title", "slug", "publish"]


@admin.register(Licence)
class LicenceAdmin(admin.ModelAdmin):
    """
    A class to represent an article.

    """

    list_display = ["title", "slug", "open"]


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """
    A class to represent an article.

    """

    list_display = ["name", "firstname", "group", "slug"]

    prepopulated_fields = {"slug": ("name", "firstname")}


class ImageProjectAdmin(admin.StackedInline):
    """
    A class to represent an article.

    """

    model = ImageProject


@admin.register(Project)
class ProjectAdmin(AdminVideoMixin, admin.ModelAdmin):
    """
    A class to represent an project.
    """

    inlines = [ImageProjectAdmin]
    list_display = ["title", "publish", "slug"]


class ImagesArticleAdmin(admin.StackedInline):
    """
    A class to represent an article.

    """

    model = ImageArticle


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """
    A class to represent an article.

    """

    inlines = [ImagesArticleAdmin]
    list_display = ["title", "publish", "slug"]
