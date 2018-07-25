from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100,verbose_name="博客标题")  # 博客标题
    category = models.CharField(max_length=50, blank=True,verbose_name="博客标签")  # 博客标签
    pub_date = models.DateTimeField(auto_now_add=True, editable=True,verbose_name="发布日期")  # 博客发布日期
    update_time = models.DateTimeField(auto_now=True, null=True,verbose_name='更新时间')
    # content = models.TextField(blank=True, null=True)  # 博客文章正文
    content = UEditorField("文章正文", height=300, width=1000, default=u'', blank=True, imagePath="uploads/my_blog/images/",
                           toolbars='besttome', filePath='uploads/my_blog/files/')
    def __unicode__(self):
        return self.title

    class Meta:  # 按时间下降排序
        ordering = ['-pub_date']
        verbose_name = "文章"
        verbose_name_plural = "文章"
