from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('works/', views.works, name='works'),
    path('blog/', views.blog, name='blog'),
]