from django.urls import path
from . import views

urlpatterns = [
    path("team_index", views.team_index, name="team_index"),
    path("team_create", views.team_create, name="team_create"),
    path("team_update/<int:pk>/", views.team_update, name="team_update"),
    # path("<category>/", views.blog_category, name="blog_category"),
]