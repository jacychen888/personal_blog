from django.contrib.syndication.views import Feed
from django.urls import reverse

from blog.models import BlogPost


class BlogRssFeed(Feed):

    title = "XiaoK的个人博客"
    link = "/rss/"

    def items(self):
        return BlogPost.objects.all()

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body

    def item_link(self, item):
        return reverse('blog_id', args=[item.id, ])
