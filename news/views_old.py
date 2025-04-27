# class-based views (CBV).
from django.shortcuts import render, redirect, get_object_or_404
from .models import Author, Book

from .forms import AuthorForm, BookForm

# AUTHORS
def author_list(request):
    authors = Author.objects.all()
    return render(request, 'news/author_list.html', {'authors': authors})

def author_create(request):
    form = AuthorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('author_list')
    return render(request, 'news/form.html', {'form': form})

def author_update(request, pk):
    author = get_object_or_404(Author, pk=pk)
    form = AuthorForm(request.POST or None, instance=author)
    if form.is_valid():
        form.save()
        return redirect('author_list')
    return render(request, 'news/form.html', {'form': form})

def author_delete(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        author.delete()
        return redirect('author_list')
    return render(request, 'news/confirm_delete.html', {'object': author})

# BOOKS
def book_list(request):
    books = Book.objects.select_related('author').all()
    return render(request, 'news/book_list.html', {'books': books})

def book_create(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, 'news/form.html', {'form': form})

def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, 'news/form.html', {'form': form})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'news/confirm_delete.html', {'object': book})

