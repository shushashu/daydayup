from django.contrib import admin

from .models import *


# Register your models here.

class StoryPicTabular(admin.TabularInline):
    model = StoryPic
    fields = (
        'pic_id',
        'pic_url',
        'pic_title'
    )

class HistoryStoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'pic_no', 'pic_no')

    inlines = [
        StoryPicTabular,
    ]


admin.site.register(HistoryStory, HistoryStoryAdmin)
admin.site.register(StoryPic)
