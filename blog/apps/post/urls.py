from django.urls import path
import apps.post.views as views

app_name = 'post'

urlpatterns = [
    path('posts/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('posts/<slug:slug>/update', views.PostDetailView.as_view(), name='post_update'),
    path('posts/<slug:slug>/delete', views.PostDetailView.as_view(), name='post_delete'),
    
]
    
