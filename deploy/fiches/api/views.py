from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response

from fiches.models import (
    Project,
    Article,
    Author,
    Notion,
    Licence,
    ImageProject,
    ImageArticle,
)

from fiches.api.serializers import (
    ProjectSerializer,
    ArticleSerializer,
    AuthorSerializer,
    NotionSerializer,
    LicenceSerializer,
    ImageProjectSerializer,
    ImageArticleSerializer,
    ImagesSerializer,
)

# ----------------------------
# images
# ----------------------------

class ImagesViewSet(ReadOnlyModelViewSet):

    serializer_class = ImagesSerializer

    def get_queryset(self):
        return ImageProject.objects

# ----------------------------
# search
# ----------------------------


class SearchView(ListAPIView):
    queryset = Project.objects.filter(publish=True).order_by("id")
    serializer_class = ProjectSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = [
        "title",
        "description",
    ]


# ----------------------------
# index
# ----------------------------


# @api_view(["GET"])
# def indexViewSet(request):
#     if request.method == "GET":
#         projects = Project.objects.filter(publish=True).order_by("title")
#         articles = Article.objects.filter(publish=True).order_by("title")

#         projects_serializer = ProjectSerializer(
#             projects, many=True, context={"request": request}
#         )

#         articles_serializer = ArticleSerializer(
#             articles, many=True, context={"request": request}
#         )

#         data = projects_serializer.data + articles_serializer.data

# return Response(data)


# ----------------------------
# notions
# ----------------------------


class NotionViewSet(ReadOnlyModelViewSet):

    serializer_class = NotionSerializer
    lookup_field = "slug"

    def get_queryset(self):
        return Notion.objects.filter(publish=True).order_by("title")


# ----------------------------
# licences
# ----------------------------


class LicenceViewSet(ReadOnlyModelViewSet):

    serializer_class = LicenceSerializer
    lookup_field = "slug"

    def get_queryset(self):
        return Licence.objects.order_by("title")


# ----------------------------
# projects
# ----------------------------


class ProjectViewSet(ReadOnlyModelViewSet):

    serializer_class = ProjectSerializer
    lookup_field = "slug"

    def get_queryset(self):
        return Project.objects.filter(publish=True).order_by("title")


class ProjectsByYear(ListAPIView):

    serializer_class = ProjectSerializer

    def get_queryset(self):
        """
        Restricts the returned notion to a given project,
        by filtering against a `notion` query parameter in the URL.
        """
        year = self.kwargs["year"]
        queryset = Project.objects.filter(date_creation__year=year)
        return queryset


class ProjectsByNotion(ListAPIView):

    serializer_class = ProjectSerializer

    def get_queryset(self):
        """
        Restricts the returned notion to a given project,
        by filtering against a `notion` query parameter in the URL.
        """
        notion_id = self.kwargs["notion_id"]
        queryset = Project.objects.filter(notion=notion_id)
        return queryset


class ProjectsByAuthor(ListAPIView):

    serializer_class = ProjectSerializer

    def get_queryset(self):
        """
        Restricts the returned notion to a given project,
        by filtering against a `notion` query parameter in the URL.
        """
        author_id = self.kwargs["author_id"]
        queryset = Project.objects.filter(author=author_id)
        return queryset


class ProjectsByUsage(ListAPIView):

    serializer_class = ProjectSerializer

    def get_queryset(self):
        """
        Restricts the returned notion to a given project,
        by filtering against a `notion` query parameter in the URL.
        """
        usage_name = self.kwargs["usage_name"]
        queryset = Project.objects.filter(usage=usage_name)
        return queryset


class ProjectsByTemporality(ListAPIView):

    serializer_class = ProjectSerializer

    def get_queryset(self):
        """
        Restricts the returned notion to a given project,
        by filtering against a `notion` query parameter in the URL.
        """
        temporality_name = self.kwargs["temporality_name"]
        queryset = Project.objects.filter(temporality=temporality_name)
        return queryset


class ProjectsByEnvironnement(ListAPIView):

    serializer_class = ProjectSerializer

    def get_queryset(self):
        """
        Restricts the returned notion to a given project,
        by filtering against a `notion` query parameter in the URL.
        """
        environnement_name = self.kwargs["environnement_name"]
        queryset = Project.objects.filter(environnement=environnement_name)
        return queryset


# ----------------------------
# articles
# ----------------------------


class ArticleViewSet(ReadOnlyModelViewSet):

    serializer_class = ArticleSerializer
    lookup_field = "slug"

    def get_queryset(self):
        return Article.objects.filter(publish=True).order_by("title")


# ----------------------------
# authors
# ----------------------------


class AuthorViewSet(ReadOnlyModelViewSet):

    serializer_class = AuthorSerializer
    lookup_field = "slug"

    def get_queryset(self):
        return Author.objects


# ----------------------------
# Images
# ----------------------------


class ImageProjectViewSet(ListAPIView):

    serializer_class = ImageProjectSerializer

    def get_queryset(self):
        project_id = self.kwargs["project_id"]
        queryset = ImageProject.objects.filter(project=project_id)
        return queryset


class ImageArticleViewSet(ListAPIView):

    serializer_class = ImageArticleSerializer

    def get_queryset(self):
        article_id = self.kwargs["article_id"]
        queryset = ImageArticle.objects.filter(article=article_id)
        return queryset
