from django.urls import path
from .views import (
    AuthorListView,
    AuthorCreateView,
    AuthorUpdateView,
    AuthorDeleteView,

    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
    CommentCreateView,
    register
)

urlpatterns = [
    path('authors/', AuthorListView.as_view(), name='author_list'),
    path('authors/create/', AuthorCreateView.as_view(), name='author_create'),
    path('authors/<int:pk>/edit/', AuthorUpdateView.as_view(), name='author_update'),
    path('authors/<int:pk>/delete/', AuthorDeleteView.as_view(), name='author_delete'),

    path('', BookListView.as_view(), name='book_list'),
    path('<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('create/', BookCreateView.as_view(), name='book_create'),
    path('<int:pk>/edit/', BookUpdateView.as_view(), name='book_update'),
    path('<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
    path('<int:book_id>/comment/', CommentCreateView.as_view(), name='add_comment'),
    path('register/', register, name='register'),
]