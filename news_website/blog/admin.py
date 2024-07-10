from django.contrib import admin

# Register your models here.
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','body','author','publish','created','updated','status',)
    list_filter = ('author','publish','status',)
    search_fields = ('title','body')
    prepopulated_fields = {'slug':('title',)}
