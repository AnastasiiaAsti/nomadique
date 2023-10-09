from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),
    path("posts/", views.posts_index, name="posts_index"),
    # path('contact/', views.about, name='about'),
]
