from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name="home"),
    path('login/',views.loginpage,name="login"),
    path('register/',views.registerUser,name='register'),
    path('logout/',views.logoutUser,name="logout"),
    path('properties',views.property,name="properties"),
    path('submit_properties/',views.submit,name="submit"),
    path('contact_us/',views.contact,name="contact"),
    path('account/',views.account,name='account'),
    path('management/',views.management,name='management'),
    path('update/<str:pk>/',views.update,name="update"),
    path('delete/<str:pk>/',views.delete_order,name="delete_order"),
    path('reopen/<str:pk>/',views.reopen_order,name="reopen_order"),
    path('orders/',views.orders,name='order'),
    path('customer<str:pk>',views.customer,name='customer'),
    path('duplex',views.duplex,name='duplex'),
    path('villa',views.villa,name='villa'),
    path('Beach_House',views.beach,name='beach'),
    path('appartments',views.appartment,name='appartment'),
    path('commercial',views.commercial,name='commercial'),
    path('rental',views.rental,name='rental'),
    path('sign/',views.sign,name='sign')
]