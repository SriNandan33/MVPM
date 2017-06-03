from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^register_property/$',views.Property_register_view,name='register_property')

]