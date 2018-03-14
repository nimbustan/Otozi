from django.contrib import admin

# Register your models here.
from blog.models import Blog


class blogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Blog,blogAdmin)