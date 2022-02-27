# from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    # Api to Post a Comment
    path('',views.bloghome,name='blogHome'),
    path('postComment',views.postComment,name='postComment'),
    path('<str:slug>',views.blogPost,name='blogPost'),
]