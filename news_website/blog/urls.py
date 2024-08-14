from django.urls import path, re_path
from .views import post_list, post_detail

app_name = "blog"

urlpatterns = [
    path("", post_list, name="post_list"),
    path("category/<slug:category_slug>/", post_list, name="category_list"),
    path("author/<int:author_pk>/", post_list, name="author_list"),
    re_path(
        r"^post/(?P<year>[0-9]+)/(?P<month>[0-9]+)/(?P<day>[0-9]{1,2})/(?P<slug>[-\w]+)/$",
        post_detail,
        name="post_detail",
    ),
    re_path(
        r"^post/(?P<year>[0-9]+)/(?P<month>[0-9]+)/(?P<day>[0-9]{1,2})/(?P<slug>[-\w]+)/comment/edit/(?P<comment_id>[0-9]+)/$",
        post_detail,
        name="comment_edit",
    ),
    re_path(r"^tag/(?P<tag_slug>[-\w]+)/", post_list, name="tag_list"),
]
