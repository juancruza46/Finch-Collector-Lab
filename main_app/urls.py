from django.urls import path
from . import views

#map out urls
urlpatterns = [
    #url endpoint, view to render, name of the route
    path('', views.home, name="home"),
    path('about/', views.about, name ='about'),
    path('finches/', views.finches_index, name = 'index'),
    path('finches/<int:finch_id>', views.finches_detail, name ="detail")
]