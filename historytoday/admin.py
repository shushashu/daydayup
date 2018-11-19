from django.contrib import admin

from .models import *


# Register your models here.


class HistoryStoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'pic_no', 'pic_no')


admin.site.register(HistoryStory, HistoryStoryAdmin)
admin.site.register(StoryPic)
