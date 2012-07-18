from api.models import Destination, Photo, Gossip
from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin

class DestinationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Destination, DestinationAdmin)
admin.site.register(Photo)
admin.site.register(Gossip, MarkdownModelAdmin)

