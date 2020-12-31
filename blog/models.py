from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class PublishedManager(models.Manager):
    def get_queryset(self):
        # calling the parent's get_queryset method
        return super(PublishedManager, self).get_queryset().filter(status="published")


class Post(models.Model):

    # default model manager
    objects = models.Manager()
    # custom model manager
    published_posts = PublishedManager()
    # first is value set in db, second is human-readable

    STATUS_CHOICES = (
        ("draft", "DRAFT"),
        ("published", "PUBLISHED"),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date="published")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    body = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")

    class Meta:
        ordering = ("-published",)

    def __str__(self):
        return self.title
