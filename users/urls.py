from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('models/', views.models_list, name='models_list'),
    path('car/<int:car_id>/', views.car_detail, name='car_detail'),
    path('available/', views.available_cars, name='available_cars'),
    
    path('contacts/', views.contacts, name='contacts'),
    path('about/', views.about, name='about'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/settings/', views.profile_settings, name='profile_settings'),
    path('password-reset/', views.password_reset, name='password_reset'),
    path('notifications/', views.notifications, name='notifications'),
]