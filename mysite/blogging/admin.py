from django.contrib import admin
from blogging.models import Post, Category


class CategoryInline(admin.TabularInline):
    "How many rows to show"
    model = Post.categories.through
    extra = 1


class PostAdmin(admin.ModelAdmin):
    "List, search fileds etc"
    inlines = [CategoryInline,]


class CategoryAdmin(admin.ModelAdmin):
    "Exclude the posts fiels"
    exclude = ('posts',)


admin.site.register(Post)
admin.site.register(Category)
