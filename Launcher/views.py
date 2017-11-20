from django.views.generic import TemplateView,ListView,DetailView,CreateView
from .models import Books,BookInstance
from .forms import BookCreateForm,BookRenewForm,BookReturnForm
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required,login_required
from django.shortcuts import get_object_or_404,render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import datetime


class Launching(TemplateView):
    template_name = 'Launcher/index.html'


class Library(TemplateView):
    template_name = 'Launcher/library_books.html'


class BooksListView(ListView):
    queryset = Books.objects.all()


class BooksDetailView(DetailView):
    model = Books


class BooksCreateView(LoginRequiredMixin,CreateView):
    form_class = BookCreateForm
    template_name = 'Launcher/form.html'
    success_url = '/library/books/'
    login_url = '/accounts/login'


class LoanedBooksByUser(LoginRequiredMixin,ListView):
    model = BookInstance
    template_name = 'Launcher/loanedBookByUser.html'

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')


class LoanedBooksByAllUsers(PermissionRequiredMixin,ListView):
    model = BookInstance
    permission_required = 'Launcher.can_mark_returned'
    template_name = 'Launcher/loanedBooksByAllUsers.html'

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o').order_by('due_back')

@permission_required('Launcher.can_mark_returned')
def renew_book_librarian(request,pk):
    book_inst = get_object_or_404(BookInstance, pk=pk)
    if request.method == 'POST':
        form = BookRenewForm(request.POST)

        if form.is_valid():
            book_inst.due_back = form.cleaned_data['due_back']
            book_inst.save()

        return HttpResponseRedirect(reverse('all-booked'))
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = BookRenewForm(initial={'renewal_date':proposed_renewal_date,})

    return render(request,'Launcher/renewbooklib.html',{'form':form,'bookinst':book_inst})


@permission_required('Launcher.can_mark_returned')
def return_book_librarian(request,pk):
    book_renew = get_object_or_404(BookInstance,pk=pk)
    if request.method == "POST":
        forming = BookReturnForm(request.POST)

        if forming.is_valid():
            book_renew.due_back=None
            book_renew.borrower=None
            book_renew.status='a'
            book_renew.save()

        return  HttpResponseRedirect(reverse('all-booked'))
    else:
        forming = BookRenewForm(request.GET)

    return render(request,'Launcher/returnBookLibrarian.html',{'form':forming,'bookinst':book_renew})
