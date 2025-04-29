from django.urls import re_path
from .views import *

urlpatterns = [
    re_path(r'^$', mobile_views, name='mobile_list'),
    re_path(r'^laptops?/$',laptop_view,name='laptop_list'), 
    re_path(r'^add_new_mobiles?/$',add_new_mobile,name='add_new_mobile'),
    re_path(r'^success/$',success_page,name = 'success_page'),
    re_path(r'^update/$',update_mobile,name='update_mobile'),
    re_path(r'^add_new_laptop?/$',add_new_Laptop,name = 'add_new_laptop' ),
    re_path(r'^update_laptop?/$', update_laptop,name='update_laptop')
]