from django.contrib import admin
from blog.models import BlogPost


# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'timeStamp']
    list_filter = ('timeStamp',)
    date_hierarchy = 'timeStamp'


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.site_header = 'XiaoK的个人博客后台管理'
admin.site.site_title = '欢迎回来,主人'
