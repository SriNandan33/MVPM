from django.conf.urls import include,url
from . import views

urlpatterns=[
    url(r'^$',views.home,name='home'),
    url(r'^login/$',views.login_view,name='login'),
    url(r'^logout/$',views.logout_view,name='logout'),
    url(r'^dashboard/$',views.dashboard,name='dashboard'),
    url(r'dashboard/notifications/$', views.all_notifications, name='all_notifications'),
    url(r'dashboard/news_updates/$',views.newsupdates,name='newsupdates'),
    url(r'dashboard/billing/$',views.billing,name='billing'),
    url(r'dashboard/profile/$',views.update_profile,name='update_profile'),
    url(r'dashboard/manage_property/',include('promanage.urls'))
]