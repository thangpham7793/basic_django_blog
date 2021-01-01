from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post


class PostListView(ListView):
    queryset = Post.published_posts.all()
    context_object_name = "posts"
    paginate_by = 1  # context contains page_obj
    template_name = "blog/post/list.html"


# def post_list(request):
#     posts = Post.published_posts.all()
#     paginator = Paginator(posts, 2)
#     page = request.GET.get("page")
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         posts = paginator.page(1)
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)
#     return render(request, "blog/post/list.html", {"page": page, "posts": posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        slug=post,
        status="published",
        published__year=year,
        published__month=month,
        published__day=day,
    )

    return render(request, "blog/post/detail.html", {"post": post})
