from django import forms
from crispy_forms.helper import FormHelper
from store.models import Book, Category, Writer

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['writer', 'category', 'name', 'slug', 'price', 'stock', 'coverpage', 'bookpage', 'description']
    

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'slug', 'icon']


class WriterForm(forms.ModelForm):
    class Meta:
        model = Writer
        fields = ['name', 'slug', 'bio', 'pic']