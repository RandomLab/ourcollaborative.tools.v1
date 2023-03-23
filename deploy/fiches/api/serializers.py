from rest_framework.serializers import ModelSerializer

from fiches.models import (
    Project,
    Article,
    Author,
    Notion,
    Licence,
    ImageProject,
    ImageArticle,
)


class ImageArticleSerializer(ModelSerializer):
    
    class Meta:
        model = ImageArticle
        fields = "__all__"


class ImageProjectSerializer(ModelSerializer):
    
    class Meta:
        model = ImageProject
        fields = "__all__"


class LicenceSerializer(ModelSerializer):

    class Meta:
        model = Licence
        fields = "__all__"


class AuthorSerializer(ModelSerializer):

    class Meta:
        model = Author
        fields = "__all__"


class NotionSerializer(ModelSerializer):

    class Meta:
        model = Notion
        fields = "__all__"


class ProjectSerializer(ModelSerializer):

    # notion = NotionSerializer(many=True)
    # author = AuthorSerializer()
    # licence = LicenceSerializer()

    class Meta:
        model = Project
        fields = "__all__"
        depth = 1


class ArticleSerializer(ModelSerializer):

    notion = NotionSerializer(many=True)
    author = AuthorSerializer()
    licence = LicenceSerializer()

    class Meta:
        model = Article
        fields = "__all__"


class ImagesSerializer(ModelSerializer):

    # project = ProjectSerializer()

    class Meta:
        model = ImageProject
        fields = "__all__"
        depth = 1