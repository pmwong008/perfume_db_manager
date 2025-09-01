from django.urls import path
from . import views

urlpatterns = [
    path('', views.dbman_index, name='dbman_index'),

    # path('dbman_list/', views.dbman_list, name='dbman_list'),
    # path('dbman_search/', views.dbman_search, name='dbman_search'),
    path('dbman_create/', views.dbman_create, name='dbman_create'),
    path('dbman_update/<int:pk>/', views.dbman_update, name='dbman_update'),
    path('dbman_delete/<int:pk>/', views.dbman_delete, name='dbman_delete'),
    path('dbman_cancel/', views.dbman_cancel, name='dbman_cancel'),
]
