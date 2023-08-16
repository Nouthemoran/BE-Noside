from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.ShowAll, name='customer-list'),
    path('detail/<int:pk>/', views.ViewProduct, name='customer-detail'),
    path('create/', views.CreateProduct, name='customer-create'),
    path('update/<int:pk>/', views.UpdateProduct, name='customer-update'),
    path('delete/<int:pk>/', views.DeleteProduct, name='customer-delete'),
    path('count/', views.CountProduct, name='customer-count'),

]