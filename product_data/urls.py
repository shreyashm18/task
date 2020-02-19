from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.home,name='home' ),
    path('add/',views.add,name='add-product'),
    path('update/<int:prod_id>/',views.update_prod),
    path('delete/<int:prod_id>/',views.delete_prod),
]
