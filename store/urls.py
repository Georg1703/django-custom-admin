from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.get_lading_page, name='lading_page'),
    path('store/', views.store, name='store_page'),
    path('order/', views.order, name='order_page'),
    path('update_item/', views.update_item, name='update_item'),
    path('order_history/', views.order_history, name='order_history'),
    path('place_order/<str:order_code>/', views.place_order, name='place_order'),
    path('order_detail/<str:order_code>/', views.order_detail, name='order_detail'),
    path('store/tags/<str:tag_name>/', views.get_products_by_tag, name='get_products_by_tag'),
]
