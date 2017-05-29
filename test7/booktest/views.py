#coding=utf-8
from django.shortcuts import render,redirect
from models import BookInfo,HeroInfo,AreaInfo
from datetime import date
from django.db.models import F,Q,Sum
# Create your views here.
def index(request):

    # list=BookInfo.books.all()[0:2]
    #查询编号等于1的图书
    # list=BookInfo.books.filter(id__exact=1)
    # list = BookInfo.books.filter(id=1)
    #模糊查询
    # list=BookInfo.books.filter(btitle__contains='传')
    # list=BookInfo.books.filter(btitle__endswith='部')
    #空判断
    # list=BookInfo.books.filter(btitle__isnull=False)
    #范围查询
    # list=BookInfo.books.filter(id__in=[1,3,5])
    #比较运算符
    # list=BookInfo.books.filter(id__gt=3)#id>3
    #不等于1
    # list=BookInfo.books.exclude(id=3)
    #日期的子值
    # list=BookInfo.books.filter(bpub_date__year=1980)
    #日期比较
    # list=BookInfo.books.filter(bpub_date__gt=date(1986,1,1))

    # 关联查询
    # list=BookInfo.books.filter(heroinfo__hcontent__contains='八')
    # list=HeroInfo.objects.filter(hbook__btitle='天龙八部')
    # context={'herolist':list}
    # return render(request,'booktest/index2.html',context)

    #两个字段进行比较
    # list=BookInfo.books.filter(bread__gte=F('bcommet'))#bread>=bcommet
    # list=BookInfo.books.filter(bread__gt=F('bcommet')*2)

    #逻辑与
    #1\where bread>20 and id<3
    # list=BookInfo.books.filter(bread__gt=20,id__lt=3)
    #不存在这种查询：2\bread>20===>id<3
    # list=BookInfo.books.filter(bread__gt=20).filter(id__lt=3)
    #逻辑或
    # list=BookInfo.books.filter(Q(bread__gt=20) | Q(id__lt=3))
    #不等于2
    # list=BookInfo.books.filter(~Q(id=3))

    #聚合
    # result=BookInfo.books.aggregate(Sum('bread'))
    # result=BookInfo.books.count()
    # print result
    list = BookInfo.books.all()
    context={'booklist':list}
    return render(request,'booktest/index.html',context)

def index2(request,id):
    #print(id)# list = BookInfo.objects.filter(id=id).heroinfo_set.all()
    #list = BookInfo.books.get(pk=id).heroinfo_set.all()
    list = HeroInfo.objects.all()
    context = {'herolist':list}
    return render(request,'booktest/index2.html',context)

def hero(request):
    # list = HeroInfo.objects.filter(hgender=True,hname__contains='黄')
    # list = HeroInfo.objects.filter(hbook__btitle='天龙八部')
    # list = HeroInfo.objects.filter(Q(id__lt=5) | Q(hgender=False))
    #错误 list = HeroInfo.objects.count(hgender=False)
    list = HeroInfo.objects.filter(hgender=False).count()
    print(list)
    context = {'herolist':list}
    return render(request,'booktest/index2.html',context)

def add(request):
    book=BookInfo.books.create('流星蝴蝶剑',date(2017,1,1))
    book.save()
    return redirect('/')

def delete(request,id):
    book=BookInfo.books.get(id=id)
    book.isdelete=True
    book.save()
    return redirect('/')

def area(request):
    city=AreaInfo.objects.get(atitle='广州市')
    qulist=city.areainfo_set.all()
    sheng=city.aParent
    context={'sheng':sheng,'city':city,'qulist':qulist}
    return render(request,'booktest/area.html',context)

