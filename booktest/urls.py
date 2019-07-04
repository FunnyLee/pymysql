from django.conf.urls import include, url
from django.contrib import admin
from booktest import views

urlpatterns = [
    url(r'^index$', views.index), #首页
    url(r'^create$', views.create), #新增
    url(r'^delete(\d+)$', views.delete), #删除
    url(r'^query$', views.query), #查询
    url(r'^aggregate$', views.aggregate), #查询(聚合函数)
    url(r'^managerQuery$', views.managerQuery), #自定义管理器对象(查询)
    url(r'^managerCreate$', views.managerCreate), #自定义管理器对象(新建)
]
