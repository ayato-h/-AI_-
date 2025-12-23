# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # トップページ -> 投稿一覧
    path('post/<int:id>/', views.post_detail, name='post_detail'),  # 詳細ページ
    path('post/new/', views.post_create, name='post_create'),  # 新規作成ページ
    path('post/<int:id>/edit/', views.post_edit, name='post_edit'),  # 編集ページ
    path('post/<int:id>/delete/', views.post_delete, name='post_delete'),  # 削除ページ
]
