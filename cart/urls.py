from django.urls import path
from .import views
from .views import check_out

app_name = 'cart'

urlpatterns = [
    path('add/<int:game_id>/', views.add_cart, name='add_cart'),
    path('', views.cart_detail, name='cart_detail'),
    path('', check_out),
    path('remove/<int:game_id>/', views.remove_cart, name='remove_cart'),
    path('remove_full/<int:game_id>/', views.remove_full, name='remove_full'),
]
