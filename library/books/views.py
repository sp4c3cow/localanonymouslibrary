from django.shortcuts import render, get_object_or_404
from .models import Book
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import PostForm, CommentForm

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


# class PostDetailView(DetailView):
#     model = Book
#     template_name = 'books/post-detail.html'

def post_detail(request, pk):
    template_name = 'books/post-detail.html'
    book = get_object_or_404(Book, pk=pk)
    comments = book.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.comment = book
            new_comment.username = request.user
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    context = {'book': book,
                'comments': comments,
                'new_comment': new_comment,
                'comment_form': comment_form}

    return render(request, template_name, context)
