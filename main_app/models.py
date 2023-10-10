from django.db import models
from django.core.files import File
from urllib import request
from django.contrib.postgres.fields import ArrayField
import os


class Link(models.Model):
    url = models.URLField()
    description = models.TextField(max_length=2000)
    image_file = models.ImageField(upload_to="images")
    image_url = models.URLField()


def get_remote_image(self):
    if self.image_url and not self.image_file:
        result = request.urlretrieve(self.image_url)
        self.image_file.save(
            os.path.basename(self.image_url), File(open(result[0], "rb"))
        )
        self.save()


class Post(models.Model):
    title = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    images = ArrayField(models.ImageField(upload_to="images/"))
    link = models.ManyToManyField(Link)
    summary = models.TextField(max_length=4000)
    hashtags = ArrayField(models.CharField(max_length=200), blank=True)


class Paragraph(models.Model):
    title = models.CharField(max_length=300)
    text = models.TextField(max_length=4000)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
