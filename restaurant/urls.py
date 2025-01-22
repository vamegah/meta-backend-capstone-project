from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token


#add following lines to urlpatterns list 
urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name="about"),
    path('menu/', views.menu, name='menu'),
    path('menu-item/<int:pk>/', views.menu_item, name='menu-detail'),
    path('book/', views.Book.as_view(), name='book'),
    path('bookings/', views.bookings, name='bookings'),
    path('menu-items', views.MenuItemView.as_view(), name='menu'),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view(), name='menu-detail'),
    path('bookings', views.BookingView.as_view(), name='bookings'),
    path('bookings/<int:pk>', views.SingleBookingView.as_view(), name='booking-detail'),
]