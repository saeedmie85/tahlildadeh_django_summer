from django.urls import path
from .views import post_list, post_detail
app_name = 'blog'

urlpatterns = [
    path('',post_list, name = 'post_list'),
    path('category/<slug:category_slug>/',post_list, name = 'category_list'),
    path('post/<int:year>/<int:month>/<int:day>/<slug:slug>/',post_detail, name = 'post_detail')
]