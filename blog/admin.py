from django.contrib import admin

from blog.models import Tag, Post, ContentImage, Contact

class ContentImageInline(admin.TabularInline):
    model = ContentImage
    extra = 1 #インラインに表示するフォームの数

class PostAdmin(admin.ModelAdmin):
    inlines = [
        ContentImageInline,
    ]

# Register your models here.

admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Contact)