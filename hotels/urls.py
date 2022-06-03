from django.urls import path

from . import views

app_name = 'hotels'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.search, name='search'),
    path('index/', views.index, name='index'),
    path('<int:hotel_id>/', views.detail, name='detail'),
    path('<int:hotel_id>/<int:room_id>/', views.displayRoom, name='room'),
]
