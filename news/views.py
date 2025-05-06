from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Author, Book, Comment
from .forms import CommentForm, UserRegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save() # сохраняем пользователя
            login(request, user)  # <-- автоматически логиним его!
            messages.success(request, 'Аккаунт создан! Теперь вы можете войти в систему.')
            return redirect('book_list')  # после успешной регистрации перекидываем на домашнюю страницу
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

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


# =============================   BOOKS   =============================
class BookListView(ListView):
    model = Book
    template_name = 'news/book_list.html'
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book
    template_name = 'news/book_detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        return context

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

# =============================   Comments   =============================
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'news/form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.book = Book.objects.get(pk=self.kwargs['book_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('book_detail', kwargs={'pk': self.kwargs['book_id']})