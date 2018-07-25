from .views import TestView,HomeView,Detail
from django.conf.urls import url


urlpatterns = [
    url(r'^test/', TestView.as_view()),
    url(r'^home/', HomeView.as_view(),name='blog_home'),
    url(r'^post/(?P<id>\d+)/$', Detail,name='blog_detail')

    # url(r'^my_log/', include('my_blog.urls')),
]
