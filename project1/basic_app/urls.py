from django.conf.urls import url
from django.urls import path
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^user_logout/$', views.user_logout, name='user_logout'),
    url(r'^account_page/$', views.account_page, name='account_page'),
    url(r'^customer/', views.customer, name='customer'),
    path(r'searched_customer/<str:cus_name>/', views.searched_customer, name='searched_customer'),  
    url(r'^exportCSV/$', views.exportCSV, name='exportCSV')
]