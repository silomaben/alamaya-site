from django.urls import path
from . import views
from .views import blogView, articleDetailView



urlpatterns = [
    path('',views.home,name='home'),
    path('view_destinations',views.destinations,name='view_destinations'),
    path('packages',views.packages,name='packages'),
    path('booking',views.booking,name='booking'),
    path('about-us',views.about,name='about-us'),
    path('contact-us',views.contact,name='contact-us'),
    path('gallery',views.gallery,name='gallery'),
    path('blog',blogView.as_view(),name='blog'),
    path('article/<int:pk>',articleDetailView.as_view(),name='article_detail'),
    path('gallery/album/<str:tag>/', views.album, name='album'),
    path('destination/<str:tag>/', views.destination_details, name='destination_details'),
    path('packages/3-days-2-night-in-maasai-mara', views.package_1, name='package_1_maasaimara'),
    path('packages/6-day-tour-of-kenyas-hidden-gems', views.package_2, name='package_2_hidden_gems'),
    path('packages/13-day-magical-kenya-safari', views.package_3, name='package_3_magical_kenya'),
    path('packages/budget-camp', views.package_4, name='package_4_budget_camp'),
    path('packages/mid-range-camp', views.package_5, name='package_5_mid_range'),
]
