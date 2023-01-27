from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.loginUser, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('single/<int:pk>', views.singleview, name='singleview'),
    path('sell/<int:pk>', views.propertyform, name='propertyform'),
    path('buy/<int:pk>', views.buyform, name='buyform'),
    path('emi/<int:pk>', views.emi_request, name='emi_request'),
    path('all/', views.allProperties, name='allProperties'),
    path('userdashboard/<str:pk_test>/', views.userDashboard, name='userdashboard'),

    # ---------Admin Dashboard urls-----------------------------

    path('rAdmin/', views.dashboard, name='dashboard'),
    path('allprop/', views.properties, name='properties'),
    path('singleprop/', views.singleprop, name='singleprop'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('formUpdate/<int:id>', views.formUpdate, name='formUpdate'),
    path('logout/', views.logoutAdm, name='logoutAdm'),

    # ---------------------Bank Dashboard Urls-------------------

    path('bank/', views.bank, name='bank')

]
