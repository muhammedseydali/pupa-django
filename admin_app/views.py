from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db import models
from django.shortcuts import render, redirect, get_object_or_404

from store.models import Category, Book
from order.models import Order, OrderItem
from .forms import BookForm, CategoryForm, WriterForm



@login_required
def admin_index(request):
    # Fetch recent orders and total sales
    recent_orders = Order.objects.order_by('-created')[:10]
    total_sales = Order.objects.filter(paid=True).aggregate(total_sales=models.Sum('payable'))['total_sales'] or 0
    
    context = {
        'recent_orders': recent_orders,
        'total_sales': total_sales,
    }
    
    return render(request, 'store/admin_base.html', context)


def admin_signin(request):
    if request.user.is_authenticated:
        return redirect('store:index')
    
    if request.method == "POST":
        user = request.POST.get('user')
        password = request.POST.get('pass')
        auth = authenticate(request, username=user, password=password)
        
        if auth is not None:
            login(request, auth)
            return redirect('admin_app:admin_index')
        else:
            messages.error(request, 'Username and password do not match')
    
    return render(request, "admin_app:admin_login")


def admin_signout(request):
    logout(request)
    return redirect('store:index')	
# Create your views here.
def books_list(request):
    books = Book.objects.all()
    return render(request, 'admintemplates/books_list.html', {'books': books})


def add_book(request):
    if request.method == "POST":
        
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book added successfully!')
            return redirect('book_list')  
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = BookForm()
    
    return render(request, 'store/admin_add_books.html', {'form': form})


def edit_book(request, id):
    book = get_object_or_404(Book, pk=id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book details updated successfully!')
            return redirect('books_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'admintemplates/edit_book.html', {'form': form})

def delete_book(request, id):
    book = get_object_or_404(Book, pk=id)
    if request.method == 'POST':
        book.delete()
        messages.success(request, 'Book deleted successfully!')
        return redirect('books_list')
    return render(request, 'admintemplates/delete_book.html', {'book': book})


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category added successfully!')
            return redirect('categories_list')  # Redirect to the list of categories
    else:
        form = CategoryForm()
    return render(request, 'admintemplates/add_category.html', {'form': form})

def update_category(request, id):
    category = get_object_or_404(Category, pk=id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category updated successfully!')
            return redirect('categories_list')  # Redirect to the list of categories
    else:
        form = CategoryForm(instance=category)
    return render(request, 'admintemplates/edit_category.html', {'form': form})