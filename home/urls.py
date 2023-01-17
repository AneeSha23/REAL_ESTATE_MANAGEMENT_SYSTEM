from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('single/',views.singleview, name='singleview'),
    path('sell/', views.propertyform, name='propertyform'),
    path('buy/',views.buyform, name='buyform')
]