from django.urls import path
from . import views

urlpatterns = [
    path('', views.manage_categories, name='categories'),
    path('add/', views.add_subcategory, name='add_subcategory'),
    path(
        'edit/<int:subcategory_id>/', views.edit_subcategory, name='edit_subcategory'
    ),
    path(
        'delete/<int:subcategory_id>/', views.delete_subcategory, name='delete_subcategory'
    )
]
