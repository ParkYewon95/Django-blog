from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    # ^ : 시작 , url에 post문자포함, pk변수에 값을 넣어 뷰에 전송, d: 숫자0~9
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/comments/$', views.comment_new, name='post_comment'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
#    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
]
