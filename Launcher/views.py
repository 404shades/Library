from django.views.generic import TemplateView,ListView,DetailView,CreateView
from .models import Books
from .forms import BookCreateForm


class Launching(TemplateView):
    template_name = 'Launcher/index.html'


class Library(TemplateView):
    template_name = 'Launcher/library_books.html'


class BooksListView(ListView):
    queryset = Books.objects.all()


class BooksDetailView(DetailView):
    queryset = Books.objects.all()


class BooksCreateView(CreateView):
    form_class = BookCreateForm
    template_name = 'Launcher/form.html'
    success_url = '/library/books/'