from django.views.generic import ListView, DetailView
from .models import News


class PostList(ListView):
    model = News
    ordering = 'name'
    template_name = 'posts.html'
    context_object_name = 'news'
    queryset = News.objects.all().order_by('-dateCreation')
    paginate_by = 10


class PostDetail(DetailView):
    model = News
    template_name = 'post.html'
    context_object_name = 'news'
