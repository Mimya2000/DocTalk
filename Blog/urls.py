from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogs, name='blogs'),
    path('blog/<str:pk>/', views.singleBlog, name='single-blog'),
]