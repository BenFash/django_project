from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post

# Create your views here.
# class based view
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6



## function based view
def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    # this is a shortcut to get data or raise a https404error # same as render being a shortcut to load data to a templ and return it. 
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post, 
            "coder": "Ben Fashan",
            "comments": comments,
            "comment_count": comment_count,
        },
    )