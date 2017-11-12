from django import forms
from .models import Books

class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = [
            'Book_Title',
            'ISBN',
            'page_amount',
        ]
    def clean_Book_Title(self):
        title = self.cleaned_data.get("Book_Title").capitalize()
        findOut = Books.objects.all()
        for i in range(0,findOut.count()):
            if title==findOut[i].getBookTitle().capitalize():
                raise forms.ValidationError("Book Title Already In Use")
        return title
