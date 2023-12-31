from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.ShowAll, name='journal-list'),
    path('detail/<int:pk>/', views.ViewProduct, name='journal-detail'),
    path('create/', views.CreateProduct, name='journal-create'),
    path('update/<int:pk>/', views.UpdateProduct, name='journal-update'),
    path('delete/<int:pk>/', views.DeleteProduct, name='journal-delete'),
    path('count/', views.CountProduct, name='journal-count'),
    path('search/', views.search_view, name='journal-search'),
    path('download_excel/', views.download_excel, name='download_journals_excel'),

]