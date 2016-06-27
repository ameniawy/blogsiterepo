from django.contrib import admin
from .models import Comment

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
	list_display = ('post',)

admin.site.register(Comment, BlogAdmin)

