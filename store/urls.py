from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.get_lading_page, name='lading_page'),
    path('store/', views.store, name='store_page'),
    path('order/', views.order, name='order_page'),
    path('update_item/', views.update_item, name='update_item'),
]
