from django.contrib import admin
from .models import Post,Category, Author, PostCategory

class PostCategoryInLine(admin.TabularInline):
    model = PostCategory
    fk_name = 'post'
    extra = 1

class PostAdmin(admin.ModelAdmin):
    inlines = [PostCategoryInLine]

admin.site.register(Category)
#admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Post,PostAdmin)
