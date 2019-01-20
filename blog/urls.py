from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name='about'),
    path('create_post/', views.PostCreateView.as_view(), name='create_post'),
    path('<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('update/<slug:slug>/', views.PostUpdateView.as_view(), name='post_update'),
    path('delete/<slug:slug>/', views.PostDeleteView.as_view(), name='post_delete'),
    path('<str:username>/posts/',
         views.AuthorListView.as_view(), name='author_posts'),
]
