from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("", views.create), # 게시글을 생성하는 URL
    path("detail/<int:article_pk>/", views.detail), # 게시글을 생성하는 URL
    path("update/<int:article_pk>/", views.update_delete), # 삭제 또는 수정하는 URL
    path('<int:article_pk>/comment/create/', views.comment_create),
    path('<int:article_pk>/comment/delete/<int:comment_pk>/', views.comment_delete),
    # path('<int:article_pk>/like/', views.like),
    
]
