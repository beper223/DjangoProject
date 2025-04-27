from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Author, Book

class AuthorListView(ListView):
    model = Author
    template_name = 'news/author_list.html'
    context_object_name = 'authors'


class AuthorCreateView(CreateView):
    model = Author
    fields = ['name']
    template_name = 'news/form.html'
    success_url = reverse_lazy('author_list')


class AuthorUpdateView(UpdateView):
    model = Author
    fields = ['name']
    template_name = 'news/form.html'
    success_url = reverse_lazy('author_list')


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'news/confirm_delete.html'
    success_url = reverse_lazy('author_list')


# BOOKS
class BookListView(ListView):
    model = Book
    template_name = 'news/book_list.html'
    context_object_name = 'books'


class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author']
    template_name = 'news/form.html'
    success_url = reverse_lazy('book_list')


class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'author']
    template_name = 'news/form.html'
    success_url = reverse_lazy('book_list')


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'news/confirm_delete.html'
    success_url = reverse_lazy('book_list')