from django.urls import path
from . import views

#map out urls
urlpatterns = [
    #url endpoint, view to render, name of the route
    path('', views.home, name="home"),
    path('about/', views.about, name ='about'),
    path('finches/', views.finches_index, name = 'index'),
    path('finches/<int:finch_id>', views.finches_detail, name ="detail"),
    path('finches/create', views.FinchCreate.as_view(), name ="finches_create"),
    path('finches/<int:pk>/update', views.FinchUpdate.as_view(), name='finches_update'),
    path('finches/<int:pk>/delete', views.FinchDelete.as_view(), name='finches_delete'),
    path('finchess/<int:finch_id>/add_feeding', views.add_feeding, name='add_feeding'),
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
]