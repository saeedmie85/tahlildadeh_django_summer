from django.urls import path
from .views import PostList

app_name = "cadmin"

urlpatterns = [
    path("", PostList.as_view(), name="post_list"),
]
