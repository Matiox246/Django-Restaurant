from django.urls import path
from . import views
from .views import BlogCreateView, BlogListView, SearchResultView, BlogUpdateView

app_name = "blog"

urlpatterns = [
    path("", BlogListView.as_view(), name='blog_list'),
    path('<slug:slug>/', views.blog_detail, name="blog_detail"),
    path('tag/<slug:tag>/', views.blog_tag, name="tag"),
    path("category/<slug:category>", views.blog_category, name="category"), 
    path('sr', SearchResultView.as_view(), name='search'),
    path('add', BlogCreateView.as_view(), name="create_blog"),
    path('update/<int:pk>', BlogUpdateView.as_view(), name="update_blog"),
]