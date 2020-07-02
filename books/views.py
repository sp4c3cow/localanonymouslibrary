from django.shortcuts import render
from .models import Book
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import PostForm

def index(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'home.html', context)


class PostListView(ListView):
    model = Book
    template_name = 'home.html'
    context_object_name = 'books'
    ordering = ['-date_posted']
    paginate_by = 12

class CreatePostView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = PostForm
    template_name = 'books/post.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDetailView(DetailView):
    model = Book
    template_name = 'books/post-detail.html'

