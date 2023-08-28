from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display=('title','slug','author','published_at','status')
    search_fields=('title','body')
    list_filter=('status','created_at','published_at','author')
    prepopulated_fields={'slug':('title',)}
    raw_id_fields=('author',)
    date_hierarchy='published_at'
    ordering=['published_at','status']




admin.site.register(Post,PostAdmin)
