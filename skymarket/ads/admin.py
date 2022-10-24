from django.contrib import admin

from ads.models import Ad, Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ("pk", "text", "author")


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):

    list_display = ("pk", "title", "price", "image", "author")
