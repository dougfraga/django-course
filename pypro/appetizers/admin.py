from django.contrib.admin import ModelAdmin, register

from pypro.appetizers.models import Video


@register(Video)
class VideoAdmin(ModelAdmin):
    list_display = ('title', 'slug', 'creation', 'youtube_id')
    ordering = ('creation',)
    prepopulated_fields = {'slug': ('title',)}
