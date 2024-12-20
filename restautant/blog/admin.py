from django.contrib import admin
from . models import Blog, Category, Tag, Comment
# Register your models here.

# admin.site.register(Blog)
# admin.site.register(Category)
# admin.site.register(Tag)
# admin.site.register(Comment)

class BLogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish_at', 'is_published')
    list_filter = ['author', "category"]
    search_fields = ("title", )
    ordering = ['title']
    date_hierarchy = "publish_at"
    empty_value_display = "-empty-"

admin.site.register(Blog, BLogAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ["email", "name", "date"]
    ordering = ["date"]
    list_filter = ["blog"]

admin.site.register(Comment, CommentAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "slug"]
    search_fields = ["title"]

admin.site.register(Category, CategoryAdmin)

class TagAdmin(admin.ModelAdmin):
    list_display = ["title", "slug"]
    search_fields = ["title"]

admin.site.register(Tag, TagAdmin)
    