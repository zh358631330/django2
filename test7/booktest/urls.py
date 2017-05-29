#coding=utf-8
from django.conf.urls import url
import views

urlpatterns=[
    url('^$',views.index),
    url('^add/$',views.add),
    url('^-(\d+)/$',views.delete),
    url('^(\d+)/$',views.index2),
    url('^area/$', views.area),
    url('^hero/$',views.hero),
]
