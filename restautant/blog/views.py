from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Blog, Tag, Category, Comment
from .forms import CommentForm
from .mixins import FieldMixin, FormValidMixins, AutorAccessMixins




# Create your views here.


# def blog_list(request):
#     blogs = Blog.objects.all()

#     paginator = Paginator(blogs, 3)
#     page_number = request.GET.get("page")
#     blog_list = paginator.get_page(page_number)

#     context =  {
#         "blog_list":blog_list,
        
#     }
#     return render(request, "blog/blog_list.html", context)



def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    tags = Tag.objects.all().filter(blogs=blog)
    recents = Blog.objects.all().order_by("publish_at")[:5]
    categories = Category.objects.all()
    comments = Comment.objects.all().filter(blog=blog)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_name = form.cleaned_data["name"]
            new_email = form.cleaned_data["email"]
            new_message = form.cleaned_data["message"]


            new_comment = Comment(blog=blog, name=new_name, email=new_email, message=new_message)
            new_comment.save()

    context = {
    "blog":blog,
    "tags": tags,
    "recents":recents,
    "categories": categories,
    "comments": comments,
    }
    return render(request, "blog/blog_detail.html", context)

def blog_tag(request, tag):
    blogs = Blog.objects.filter(tags__slug=tag)

    context = {
        "blogs":blogs
    }
    return render(request, "blog/blog_list.html", context)


def blog_category(request, category):
    blogs = Blog.objects.filter(category__slug=category)

    context = {
        "blogs":blogs
    }
    return render(request, "blog/blog_list.html", context)


class SearchResultView(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        query = self.request.GET.get('search', '')
        if query:
            return Blog.objects.filter(title__icontains=query)
        return Blog.objects.all()



class BlogListView(ListView):
     model = Blog
     template_name = 'blog/blog_list.html'
     context_object_name = 'blogs'

class BlogCreateView(LoginRequiredMixin, FieldMixin, FormValidMixins, CreateView):
    model = Blog
    template_name = 'blog/create.html'
    success_url = reverse_lazy('account:blogs')

    # def form_valid(self, form):    old way to auto set autor name in blogs
    #     form.instance.author = self.request.user # Set the user to the logged-in user
    #     return super().form_valid(form)

class BlogUpdateView(AutorAccessMixins, FieldMixin, FormValidMixins, UpdateView):
    model = Blog
    template_name = 'blog/create.html'
    success_url = reverse_lazy('account:blogs')

