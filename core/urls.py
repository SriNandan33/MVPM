from django.conf.urls import  url
from . import views
urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^homes_for_rent/$',views.home_for_rent,name='homes_for_rent'),
    url(r'^homes_for_rent/(?P<id>\d+)/$', views.home_detail, name='home_detail')
]