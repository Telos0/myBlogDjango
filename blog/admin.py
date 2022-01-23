from django.contrib import admin
from .models import Post, Category, Tag, RunningServices, Comment
from markdownx.admin import MarkdownxModelAdmin

# Register your models here.

admin.site.register(Post, MarkdownxModelAdmin)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name', )}

admin.site.register(Category, CategoryAdmin)

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name', )}

admin.site.register(Tag, TagAdmin)
admin.site.register(Comment)
admin.site.register(RunningServices)