from __future__ import absolute_import
from django.contrib import admin
from .models import Post 

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'created_at', 'views')

admin.site.register(Post, PostAdmin)