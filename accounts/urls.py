from django.urls import path
from accounts import views


app_name = 'accounts'

urlpatterns = [
    # path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
]
