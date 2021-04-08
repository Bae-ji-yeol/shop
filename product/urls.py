from django.urls import path
from . import views


app_name = 'product'

urlpatterns = [
    path('', views.list, name='list'),
    path('<int:game_id>/', views.detail, name='detail'),
    path('comment/create/<int:game_id>/', views.comment_create, name='comment_create')
]