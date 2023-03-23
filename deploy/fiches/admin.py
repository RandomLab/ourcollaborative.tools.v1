from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import (
    Project,
    Author,
    Licence,
    Notion,
    Article,
    ImageArticle,
    ImageProject,
)


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

    list_display = ["name","firstname",  "group", "slug"]

    prepopulated_fields = {"slug": ("name","firstname")}


class ImageProjectAdmin(admin.StackedInline):
    """
    A class to represent an article.

    """

    model = ImageProject


@admin.register(Project)
class ProjectAdmin(AdminVideoMixin, admin.ModelAdmin):
    """
    A class to represent an article.

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
    list_display = ["title", "publish", "author", "slug"]
