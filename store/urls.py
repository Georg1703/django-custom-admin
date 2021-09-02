from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.get_lading_page, name='lading_page'),
    path('store/', views.store, name='store_page'),
    path('order/', views.order, name='order_page'),
    path('update_item/', views.update_item, name='update_item'),
    path('place_order/<int:order_id>/', views.place_order, name='place_order'),
    path('order_history/', views.order_history, name='order_history'),
    path('order_detail/<int:order_id>/', views.order_detail, name='order_detail'),
]
