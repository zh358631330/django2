#coding=utf-8


from django.db import models

# Create your models here.
class BookInfoManager(models.Manager):
    #原始查询集的更改
    def get_queryset(self):
        return super(BookInfoManager,self).get_queryset().filter(isdelete=False)
    #新增模型类的方式
    def create(self,btitle,bpub_date):
        book=BookInfo()
        book.btitle=btitle
        book.bpub_date=bpub_date
        book.bread=0
        book.bcommet=0
        book.isdelete=False
        return book

class BookInfo(models.Model):
    btitle=models.CharField(max_length=20)
    bpub_date=models.DateField()
    bread=models.IntegerField(default=0)
    bcommet=models.IntegerField(default=0)
    isdelete=models.BooleanField(default=False)
    class Meta:
        db_table='bookinfo'

    books=BookInfoManager()

class HeroInfo(models.Model):
    hname=models.CharField(max_length=20)
    hgender=models.BooleanField(default=True)
    isDelete=models.BooleanField(default=False)
    hcontent=models.CharField(max_length=100)
    hbook=models.ForeignKey('BookInfo')

class AreaInfo(models.Model):
    atitle=models.CharField(max_length=20)
    aParent=models.ForeignKey('self',null=True,blank=True)
