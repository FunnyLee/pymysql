from datetime import date

from django.db.models import F, Q, Sum, Count, Avg, Max, Min
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from booktest.models import BookInfo


def index(request):
    # 显示图书信息

    books = BookInfo.objects.all()
    return render(request, 'booktest/index.html', {"books": books})


def create(request):
    # 新增一本图书
    book = BookInfo()
    book.btitle = "倚天屠龙记"
    book.bpub_date = date(1998, 2, 5)
    book.bread = 100
    book.bcomment = 59
    book.save()
    # 重定向，服务器不返回页面，而是告诉浏览器去请求其他的url
    return HttpResponseRedirect('/index')


def delete(request, id):
    # 删除图书
    book = BookInfo.objects.get(id=id)
    book.delete()
    return HttpResponseRedirect('/index')


def query(request):
    # 查询
    # book = BookInfo.objects.get(id=1)

    query_set = BookInfo.objects.filter(btitle__exact="射雕英雄传")

    # query_set = BookInfo.objects.filter(btitle__contains='笑')

    # query_set = BookInfo.objects.filter(btitle__startswith='雪')

    # query_set = BookInfo.objects.filter(btitle__isnull=False)

    # 范围查询
    # query_set = BookInfo.objects.filter(bread__in=(12, 36, 20))

    # 比较查询
    # query_set = BookInfo.objects.filter(bread__gt=58)
    # query_set = BookInfo.objects.filter(bread__gte=58)

    # 日期查询
    # query_set = BookInfo.objects.filter(bpub_date__year=1995)

    # 对查询结果排序
    # query_set = BookInfo.objects.filter(bpub_date__gt=date(1986, 1, 1)).order_by('-id')

    # 查询不满足条件的数据
    # query_set = BookInfo.objects.exclude(bcomment__gt=30)

    # 属性之间比较，使用F类
    # query_set = BookInfo.objects.filter(bread__gt=F('bcomment'))

    # query_set = BookInfo.objects.filter(bread=12, bcomment=34)

    # 查询条件的或与非
    # query_set = BookInfo.objects.filter(Q(bread=36)&Q(bcomment=40))
    # 非
    # query_set = BookInfo.objects.filter(~Q(isDelete=0))

    book = query_set[0]

    return render(request, "booktest/query.html", {"querybook": book})


def aggregate(request):
    # 聚合函数，使用aggregate函数
    # num = BookInfo.objects.all().count() # 这个方法返回的是一个数字

    # dictionary = BookInfo.objects.aggregate(Count('id')) #这个方法返回的是一个字典

    # dictionary = BookInfo.objects.aggregate(Sum('bread')) #{'bread__sum': 126}

    # dictionary = BookInfo.objects.aggregate(Max('bcomment'))

    return render(request, 'booktest/query.html', "")


def managerQuery(request):
    '''自定义管理器对象'''

    query_set = BookInfo.objects.all()

    book = query_set[0]

    print(len(query_set))
    print(book.btitle)

    return render(request, 'booktest/query.html', "")


def managerCreate(request):
    return BookInfo.objects.createBook()
