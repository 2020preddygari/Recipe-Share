from django.urls import path
from recipes import views


urlpatterns = [
    path("create/", views.create, name="create"),
    path("<int:recipe_id>", views.detail, name="detail"),
    path("<int:recipe_id>/upvote", views.upvote, name="upvote"),
]