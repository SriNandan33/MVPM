from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^register_property/$',views.Property_register_view,name='register_property'),
    url(r'^properties/$',views.propertylist,name='property_list'),
    url(r'^properties/(?P<id>\d+)/$',views.property_detail,name='property_detail'),
    url(r'^properties/(?P<id>\d+)/post_issue',views.maintenace_request,name='maintenance_request')

]