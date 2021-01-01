from django import template
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown
from ..models import Post

register = template.Library()


@register.filter(name="markdown")
def markdown_format(text):
    return mark_safe(markdown.markdown(text))


@register.inclusion_tag("blog/post/blog_summary.html")
def show_blog_summary():
    return {"total_posts": Post.published_posts.count()}


@register.inclusion_tag("blog/post/latest_posts.html")
def show_latest_posts(count=5):
    latest_posts = Post.published_posts.order_by("-published")[:count]
    return {"latest_posts": latest_posts, "title": "Latest Posts"}


@register.inclusion_tag("blog/post/most_commented_posts.html")
def show_most_commented_posts(count=2):
    most_commented_posts = Post.published_posts.annotate(
        total_comments=Count("comments"),
    ).order_by("-total_comments")[:count]
    return {
        "most_commented_posts": most_commented_posts,
        "title": "Most Commented Posts",
    }
