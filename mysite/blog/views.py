from django.shortcuts import render
from blog.models import BlogPost
import markdown
from pure_pagination import PageNotAnInteger, Paginator


# Create your views here.
def index(request):
    blog_list = BlogPost.objects.all()  # 获取所有数据
    # 分页
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1
    p = Paginator(blog_list, 5, request=request)  # 5为每页展示的博客数目
    blog_list = p.page(page)
    blog_size = len(blog_list.object_list)
    for i in range(0, blog_size):
        content = blog_list.object_list[i].body
        blog_list.object_list[i].body = markdown.markdown(content,
                                    extensions=[
                                        'markdown.extensions.extra',
                                        'markdown.extensions.codehilite',
                                        'markdown.extensions.toc',
                                    ])

    return render(request, 'index.html', {'index': 0, 'blog_list': blog_list, 'blog_size': blog_size})


def detail(request, blog_id):
    blog = BlogPost.objects.get(id=blog_id)
    blog.body = markdown.markdown(blog.body,
                                    extensions=[
                                        'markdown.extensions.extra',
                                        'markdown.extensions.codehilite',
                                        'markdown.extensions.toc',
                                        'markdown.extensions.tables',
                                    ])
    return render(request, 'detail.html', {'index': 0, "blog": blog})


def archive(request):
    blog_list = BlogPost.objects.all().order_by('-timeStamp')
    # 分页
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1
    p = Paginator(blog_list, 10, request=request)  # 每页展示的博客数目10
    blog_list = p.page(page)
    return render(request, 'archive.html', {'index': 1, 'blog_list': blog_list})


def about(request):
    return render(request, 'about.html', {'index': 2})


def contact(request):
    return render(request, 'contact.html', {'index': 3})



