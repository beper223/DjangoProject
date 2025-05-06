from django import forms
from .models import Author, Book, Comment
# для регистрации на сайте
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# для регистрации на сайте
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Оставьте ваш комментарий...'}),
        }