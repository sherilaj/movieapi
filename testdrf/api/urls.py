
from django.urls import path

from . import views
from . views import *
urlpatterns = [
    path('',MovieList,name='movielist'),
    path('comments',CommentList,name='commentlist'),
    path('create',views.CreateUser.as_view(),name='create'),
    path('moviecomment/<int:forkey_id>/',Movie_Comment,name='moviecomment'),
    path('postcomment',views.CreateComment.as_view(),name='createcomment'),

]
