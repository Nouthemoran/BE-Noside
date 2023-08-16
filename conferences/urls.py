from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.ShowAll, name='conferences-list'),
    path('detail/<int:pk>/', views.ViewProduct, name='conferences-detail'),
    path('create/', views.CreateProduct, name='conferences-create'),
    path('update/<int:pk>/', views.UpdateProduct, name='conferences-update'),
    path('delete/<int:pk>/', views.DeleteProduct, name='conferences-delete'),
]