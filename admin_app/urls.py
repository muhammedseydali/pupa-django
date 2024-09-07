from django.urls import path
from . import views

app_name = 'admin_app'


urlpatterns = [
	path('admin_dashboard/', views.admin_index, name = "admin_index"),
	path('login', views.admin_signin, name="admin_signin"),
	path('logout', views.admin_signout, name="admin_signout"),
    path('books/', views.books_list, name='books_list'),
    path('books/add/', views.add_book, name='add_book'),
    path('books/edit/<int:id>/', views.edit_book, name='edit_book'),
    path('books/delete/<int:id>/', views.delete_book, name='delete_book'),
    path('add-category/', views.add_category, name='add_category'),
    path('update-category/<int:id>/', views.update_category, name='update_category'),
]