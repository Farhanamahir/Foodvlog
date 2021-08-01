from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name='hm'),
    path('<slug:c_slug>/', views.home, name='prod_cat'),
    path('<slug:c_slug>/<slug:products_slug>',views.prodetails,name='detail'),
    path('search',views.searching,name='search')


]