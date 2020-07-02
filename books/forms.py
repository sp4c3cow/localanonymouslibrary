from django import forms
from .models import Book, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description', 'image', 'files']
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['email', 'body']


