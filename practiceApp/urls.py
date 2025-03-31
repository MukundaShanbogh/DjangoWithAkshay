from django.urls import re_path
from .views import mobile_views,laptop_view 

urlpatterns = [
    re_path(r'^$', mobile_views, name='mobile_list'),
    re_path(r'^laptops?/$',laptop_view,name='laptop_list'), 
]