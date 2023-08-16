from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.ShowAll, name='repository-list'),
    path('detail/<int:pk>/', views.ViewProduct, name='repository-detail'),
    path('create/', views.CreateProduct, name='repository-create'),
    path('update/<int:pk>/', views.UpdateProduct, name='repository-update'),
    path('delete/<int:pk>/', views.DeleteProduct, name='repository-delete'),
    path('count/', views.CountProduct, name='repository-count'),

]