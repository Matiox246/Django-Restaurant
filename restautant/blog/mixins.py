from django.http import Http404
from django.shortcuts import get_object_or_404
from .models import Blog

class FieldMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self.fields = [
                            'author',
                            'title', 
                            'slug', 
                            'description', 
                            'content',                  
                            'image', 
                            'category', 
                            'tags', 
                            'is_published',
                            'publish_at', 
                        ]

        elif request.user.is_author:
            self.fields = [
                            'title', 
                            'slug', 
                            'description', 
                            'content', 
                            'image', 
                            'category', 
                            'tags', 
                        ]
        else:
            raise Http404("You not allowed to see this page")
        return super().dispatch(request, *args, **kwargs)
    
class FormValidMixins():
    def form_valid(self,form):
        if self.request.user.is_superuser:
            form.save()
        else:
            self.obj = form.save(commit=False)
            self.obj.author = self.request.user
            self.obj.status = 'd'
        return super().form_valid(form)
    
class AutorAccessMixins():
    def dispatch(self, request, pk, *args, **kwargs):
        blog = get_object_or_404(Blog, pk=pk)
        if blog.author == request.user and blog.is_published == False or\
              request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)            
        else:
            raise Http404("You not allowed to see this page")
       