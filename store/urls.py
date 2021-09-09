from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.get_lading_page, name='lading'),
    path('about_company/', views.get_company_page, name='company'),
    path('contact_us/', views.get_contact_us_page, name='contact_us'),
    path('order/', views.get_order_page, name='order'),
    path('products/', views.get_products_page, name='products'),

    path('place_order/<str:order_code>/', views.place_order, name='place_order'),
    path('products/<str:product_name>', views.get_product_page, name='product'),
    path('update_item/', views.update_item, name='update_item'),
    path('order_history/', views.order_history, name='order_history'),
    path('order_detail/<str:order_code>/', views.order_detail, name='order_detail'),
    path('products/tags/<str:tag_name>/', views.get_products_by_tag, name='get_products_by_tag'),
]
