from django.contrib import admin
from .models import Book, Comment

admin.site.register(Book)

# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('username', 'body', 'post', 'created_on', 'active')
#     list_filter = ('active', 'created_on')
#     search_fields = ('username', 'email', 'body')
#     actions = ['approve_comments']

#     def approve_comments(self, request, queryset):
#         queryset.update(active=True)