from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.ShowAll, name='conference-list'),
    path('detail/<int:pk>/', views.ViewProduct, name='conference-detail'),
    path('create/', views.CreateProduct, name='conference-create'),
    path('update/<int:pk>/', views.UpdateProduct, name='conference-update'),
    path('delete/<int:pk>/', views.DeleteProduct, name='conference-delete'),
    path('count/', views.CountProduct, name='conference-count'),
    path('search/', views.search_view, name='conference-search'),
    path('download_excel/', views.download_excel, name='download_conferences_excel'),

]