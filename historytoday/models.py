from django.db import models

__all__ = [
    'HistoryStory',
    'StoryPic',
]


# Create your models here.

class HistoryStory(models.Model):
    e_id = models.SmallIntegerField('_id', blank=False, null=True)
    title = models.CharField('标题', max_length=64, blank=False, null=True)
    content = models.TextField('正文呢', max_length=1024, blank=False, null=True)
    pic_no = models.SmallIntegerField('图片数量', blank=False, null=True)
    date = models.CharField('日期', max_length=20, blank=False, null=True)
    day = models.CharField('日期', max_length=10, blank=False, null=True)

    class Meta:
        verbose_name = '历史上的今天'
        verbose_name_plural = verbose_name
        db_table = 'hero_history_story'

    def __str__(self):
        return self.title


class StoryPic(models.Model):
    story = models.ForeignKey('HistoryStory', on_delete=models.CASCADE, verbose_name='文章')
    pic_id = models.SmallIntegerField('插图ID', blank=False, null=True)
    pic_url = models.URLField('图片地址', blank=False, null=True)
    pic_title = models.CharField('图片标题', max_length=32, blank=False, null=True)

    class Meta:
        verbose_name = '事件插图'
        verbose_name_plural = verbose_name
        db_table = 'hero_history_pic'

    def __str__(self):
        return self.pic_title
