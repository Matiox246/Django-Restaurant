from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Article, Tag, Category, Comment
from .forms import CommentForm
from .mixins import FieldMixin, FormValidMixins, AutorAccessMixins




# Create your views here.


class ArticleListView(ListView):
    model = Article
    paginate_by = 3
    queryset = Article.objects.order_by('-publish_at')



def blog_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    tags = Tag.objects.all().filter(blogs=article)
    recents = Article.objects.all().order_by("publish_at")[:5]
    categories = Category.objects.all()
    comments = Comment.objects.all().filter(article=article)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_name = form.cleaned_data["name"]
            new_email = form.cleaned_data["email"]
            new_message = form.cleaned_data["message"]


            new_comment = Comment(article=article, name=new_name, email=new_email, message=new_message)
            new_comment.save()

    context = {
    "article":article,
    "tags": tags,
    "recents":recents,
    "categories": categories,
    "comments": comments,
    }
    return render(request, "blog/article_detail.html", context)


def blog_tag(request, tag):
    blogs = Article.objects.filter(tags__slug=tag)
    context = {
        "blogs":blogs
    }
    return render(request, "blog/blog_list.html", context)


def blog_category(request, category):
    blogs = Article.objects.filter(category__slug=category)
    context = {
        "blogs":blogs
    }
    return render(request, "blog/blog_list.html", context)


class SearchResultView(ListView):
    model = Article
    paginate_by = 3
    template_name = 'blog/search_result.html'
    context_object_name = 'articles'

    def get_queryset(self):
        query = self.request.GET.get('search', '')
        if query:
            return Article.objects.filter(title__icontains=query)
        return Article.objects.all()




class BlogCreateView(LoginRequiredMixin, FieldMixin, FormValidMixins, CreateView):
    model = Article
    success_url = reverse_lazy('account:blogs')


class BlogUpdateView(AutorAccessMixins, FieldMixin, FormValidMixins, UpdateView):
    model = Article
    template_name = 'blog/create.html'
    success_url = reverse_lazy('account:blogs')

