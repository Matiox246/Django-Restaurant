from django.contrib import admin
from . models import Article, Category, Tag, Comment


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish_at', 'is_published')
    list_filter = ['author', "category"]
    search_fields = ("title", )
    ordering = ['title']
    date_hierarchy = "publish_at"
    empty_value_display = "-empty-"

admin.site.register(Article, ArticleAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ["email", "name", "date"]
    ordering = ["date"]
    list_filter = ["article"]
admin.site.register(Comment, CommentAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "slug"]
    search_fields = ["title"]

admin.site.register(Category, CategoryAdmin)

class TagAdmin(admin.ModelAdmin):
    list_display = ["title", "slug"]
    search_fields = ["title"]

admin.site.register(Tag, TagAdmin)
    