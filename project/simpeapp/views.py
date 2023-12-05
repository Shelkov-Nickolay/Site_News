from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .models import News
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from .filters import NewsFilter
from .forms import NewsForm


class PostList(ListView):
    model = News
    ordering = 'name'
    template_name = 'posts.html'
    context_object_name = 'news'
    queryset = News.objects.all().order_by('-dateCreation')
    paginate_by = 3


class PostDetail(DetailView):
    model = News
    template_name = 'post.html'
    context_object_name = 'news'


class Search(ListView):
    model = News
    ordering = 'name'
    template_name = 'search.html'
    context_object_name = 'news'
    queryset = News.objects.all().order_by('-dateCreation')
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class NewsCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('simpeapp.add_news',)
    form_class = NewsForm
    model = News
    template_name = 'news_edit.html'

    def form_valid(self, form):
        news = form.save(commit=False)
        news.categoryType = 'NW'
        return super().form_valid(form)


class ArticlesCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('simpeapp.add_news',)
    form_class = NewsForm
    model = News
    template_name = 'articles_edit.html'

    def form_valid(self, form):
        news = form.save(commit=False)
        news.categoryType = 'AR'
        return super().form_valid(form)


class NewsUpdate(LoginRequiredMixin, PermissionRequiredMixin,  UpdateView):
    permission_required = ('simpeapp.change_news',)
    raise_exception = True
    form_class = NewsForm
    model = News
    template_name = 'news_edit.html'


class ArticlesUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ('simpeapp.change_news',)
    raise_exception = True
    form_class = NewsForm
    model = News
    template_name = 'articles_edit.html'


class NewsDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ('simpeapp.delete_news',)
    raise_exception = True
    model = News
    template_name = 'product_delete.html'
    success_url = reverse_lazy('post_list')


class ArticlesDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ('simpeapp.delete_news',)
    raise_exception = True
    model = News
    template_name = 'product_delete.html'
    success_url = reverse_lazy('post_list')
