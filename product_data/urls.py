from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('',views.home,name='home' ),
    path('add/',views.add,name='add-product'),
    path('update/<int:prod_id>/',views.update_prod),
    path('delete/<int:prod_id>/',views.delete_prod),
    path('register/', views.register, name="register"),
    path('login/', auth_view.LoginView.as_view(), name='login'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),
]
