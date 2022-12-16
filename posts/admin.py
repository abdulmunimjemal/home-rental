from django.contrib import admin
from .models import Post, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class PostAdmin(admin.ModelAdmin):
    inlines = [ 
               CommentInline
               ]
    model = Post
    list_display = ['title', 'category', 'rental_rate', 'town', 'region', 'author', 'created_on']
    list_filter = ('category', 'region')
    search_fields = ('title', 'author', 'body', 'address', 'town')

class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ('ad', 'author', 'comment')
    list_filter = ['ad','author']
    search_fields = ('comment',)
    
# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
