from django.contrib import admin
from .models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('text', 'author', 'pub_date', 'likes', 'comments')
    fields = ('text', 'author', 'pub_date', 'likes', 'comments')

admin.site.register(Post, PostAdmin)