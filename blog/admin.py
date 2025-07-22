from django.contrib import admin
from blog.models import Post, Comment
from django.contrib import admin

import admin_thumbnails

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

# Register your models here.
@admin.register(Post)
@admin_thumbnails.thumbnail('thumbnail')
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'thumbnail']

    inlines = [
        CommentInline,
    ]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass