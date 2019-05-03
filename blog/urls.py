from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    url(r'^$', views.blogs_list_view, name='blog_list_view'),
    url(r'^blog/(?P<pk>[0-9]+)/$', views.blogs_detail_view, name='blog_detail_view'),
    url(r'blog/create/$', login_required(views.create_new_blog, login_url="/accounts/login/"), name='create_new_blog'),
    url(r'^blog/(?P<pk>[0-9]+)/edit/$', login_required(views.edit_blog, login_url="/accounts/login/"),
        name='edit_blog'),
    url(r'blog/(?P<pk>[0-9]+)/delete/$', login_required(views.delete_blog, login_url="/accounts/login/"),
        name='delete_blog')
]
