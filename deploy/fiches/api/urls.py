from django.urls import path
from django.conf.urls import include
from rest_framework import routers

from fiches.api.views import (

    SearchProjectView,
    SearchNotionView,

    ProjectViewSet,
    ArticleViewSet,
    AuthorViewSet,
    NotionViewSet,
    LicenceViewSet,

    ImageArticleViewSet,
    ImageProjectViewSet,
    ImagesViewSet,

    ProjectsByNotion,
    ProjectsByAuthor,
    ProjectsByUsage,
    ProjectsByTemporality,
    ProjectsByEnvironnement,
    ProjectsByYear
)

images_router = routers.SimpleRouter()
images_router.register("images", ImagesViewSet, basename="images")

project_router = routers.SimpleRouter()
project_router.register("project", ProjectViewSet, basename="project")

article_router = routers.SimpleRouter()
article_router.register("article", ArticleViewSet, basename="article")

author_router = routers.SimpleRouter()
author_router.register("author", AuthorViewSet, basename="author")

notion_router = routers.SimpleRouter()
notion_router.register("notion", NotionViewSet, basename="notion")

licence_router = routers.SimpleRouter()
licence_router.register("licence", LicenceViewSet, basename="licence")

urlpatterns = [
    path("search_projects/", SearchProjectView.as_view()),
    path("search_notions/", SearchNotionView.as_view()),

    path("", include(images_router.urls)),
    path("", include(project_router.urls)),
    path("", include(article_router.urls)),
    path("", include(author_router.urls)),
    path("", include(notion_router.urls)),
    path("", include(licence_router.urls)),

    path("image_project/<int:project_id>/", ImageProjectViewSet.as_view()),
    path("image_article/<int:article_id>/", ImageArticleViewSet.as_view()),

    path("projects_by_notion/<int:notion_id>/", ProjectsByNotion.as_view()),
    path("projects_by_author/<int:author_id>/", ProjectsByAuthor.as_view()),

    path("projects_by_usage/<str:usage_name>/", ProjectsByUsage.as_view()),
    path("projects_by_temporality/<str:temporality_name>/", ProjectsByTemporality().as_view()),
    path("projects_by_environnement/<str:environnement_name>/", ProjectsByEnvironnement().as_view()),

    path("projects_by_year/<str:year>/", ProjectsByYear().as_view())
]
