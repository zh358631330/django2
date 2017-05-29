from django.conf.urls import url
import views
urlpatterns=[
    url('^$',views.index ,name='index'),
    url('^area1/$',views.area1),
    url('^area2/$', views.sheng),

    url('^area3/$',views.shi),
    url('^pic_upload/$',views.pic_upload),
    url('^pic_handle/$',views.pic_handle),
    url('^pic_show/$',views.pic_show),
    url(r'^page(?P<pIndex>[0-9]*)/$', views.page_test),
]
