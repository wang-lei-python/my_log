from django.contrib import admin

# Register your models here.
from my_blog.models import Article

#注册自己的模型类
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date')

admin.site.register(Article,ArticleAdmin)