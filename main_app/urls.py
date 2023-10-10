from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),
    path("map/", views.map, name="map"),
    path("posts/", views.posts_index, name="posts_index"),
    path("posts/detail", views.posts_detail, name="posts_detail"),
    path("thrifts/", views.thrifts_index, name="thrifts_index"),
    path("deals/", views.deals_index, name="deals_index"),
]
