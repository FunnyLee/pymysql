from datetime import date

from django.db import models

# Create your models here.
from django.http import HttpResponseRedirect


class BookInfoMananger(models.Manager):
    '''自定管理器'''

    # def all(self):
    #     return super().all().filter(btitle__contains='射')

    def createBook(self):
        book = BookInfo()
        book.btitle = "鹿鼎记"
        book.bpub_date = date(1994, 5, 21)
        book.bread = 100
        book.bcomment = 50
        book.save()
        return HttpResponseRedirect('/index')


class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField()
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)

    # 自定义管理器
    objects = BookInfoMananger()


class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=True)
    hcomment = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    hbook = models.ForeignKey('BookInfo')
