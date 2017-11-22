from django import forms
from .models import Books,BookInstance,Profile
import datetime
from registration.forms import RegistrationFormUniqueEmail


class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = [
            'Book_Title',
            'ISBN',
            'page_amount',
            'subj_code'
        ]
    def clean_Book_Title(self):
        title = self.cleaned_data.get("Book_Title").capitalize()
        findOut = Books.objects.all()
        for i in range(0,findOut.count()):
            if title==findOut[i].getBookTitle().capitalize():
                raise forms.ValidationError("Book Title Already In Use")
        return title

class BookRenewForm(forms.ModelForm):
    class Meta:
        model = BookInstance
        fields = [
            'due_back',
        ]

    def clean_renewal_date(self):
        data = self.cleaned_data.get('due_back')
        if data < datetime.date.today():
            raise forms.ValidationError('Invalid Date Renewal in Past')
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise forms.ValidationError("Invalid Date Renewal more than 4 weeks")

        return data


class BookReturnForm(forms.ModelForm):
    class Meta:
        model = BookInstance
        fields = [
            'borrower'
        ]

    def clean_borrower(self):
        data = self.cleaned_data.get('borrower')
        return data


class ProfileForm(RegistrationFormUniqueEmail):
    roll_number = forms.IntegerField()

    def clean_roll_number(self):
        roll = self.cleaned_data.get('roll_number')
        if roll == 1:
            raise forms.ValidationError('Invalid Roll Number')
        return roll