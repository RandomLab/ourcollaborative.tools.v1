from rest_framework.serializers import ModelSerializer

from fiches.models import (
    Project,
    Article,
    Author,
    Notion,
    Licence,
    Reference,
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


class ReferenceSerializer(ModelSerializer):
    class Meta:
        model = Reference
        fields = "__all__"

    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     data["type"] = "reference"
    #     return data


class LicenceSerializer(ModelSerializer):
    class Meta:
        model = Licence
        fields = "__all__"


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["type"] = "author"
        return data


class NotionSerializer(ModelSerializer):
    class Meta:
        model = Notion
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["type"] = "notion"
        return data


class ProjectSerializer(ModelSerializer):

    # notion = NotionSerializer(many=True)
    # author = AuthorSerializer()
    # licence = LicenceSerializer()

    class Meta:
        model = Project
        fields = "__all__"
        depth = 1

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["type"] = "project"
        return data


class ArticleSerializer(ModelSerializer):

    # notion = NotionSerializer(many=True)
    # author = AuthorSerializer()
    # licence = LicenceSerializer()

    class Meta:
        model = Article
        fields = "__all__"
        depth = 1

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["type"] = "article"
        return data


class ImagesSerializer(ModelSerializer):

    # project = ProjectSerializer()

    class Meta:
        model = ImageProject
        fields = "__all__"
        depth = 1
