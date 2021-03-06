from django.db import models
from django.db.models.signals import pre_save
from .utils import unique_slug_generator
from django.contrib.auth.models import User
import uuid
from datetime import date


class Subject(models.Model):
    name = models.CharField(max_length=200,help_text="Enter Subject Name (e.g Film, Studio, Television)")

    def __str__(self):
        return self.name


class Books(models.Model):
    Book_Title      = models.CharField(max_length=250)
    ISBN            = models.CharField(max_length=250,null=True,blank=True)
    Author_Name     = models.CharField(max_length=250,null=True,blank=True)
    page_amount     = models.CharField(max_length=250,null=True,blank=True)
    Year            = models.CharField(max_length=250,null=True,blank=True)
    Publisher_Name  = models.CharField(max_length=250,null=True,blank=True)
    slug            = models.SlugField(blank=True, null=True,max_length=250)
    subj_code       = models.ForeignKey(Subject,help_text="Select Subject of the book",default=None,null=True,blank=True)

    def __str__(self):
        return self.Book_Title

    @property
    def title(self):
        return self.Book_Title

    def getBookTitle(self):
        return self.Book_Title

    def get_subject(self):
        return self.subj_code


def rl_pre_save_receiver(sender,instance,**kwargs):
    instance.Book_Title = instance.Book_Title.capitalize()
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
        instance.save()


pre_save.connect(rl_pre_save_receiver,sender=Books)


class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,unique=True,help_text="Unique Id For the Particular book across whole library")
    book = models.ForeignKey('Books', on_delete=models.CASCADE,null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False

    @property
    def calculate_fine(self):
        delta = date.today() - self.due_back
        return delta.days

    LOAN_STATUS = (
        ('m', 'On Maintainence'),
        ('o', 'On Loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status =    models.CharField(max_length=1,choices=LOAN_STATUS,blank=True,default='a',help_text="Book Availablity")

    class Meta:
        ordering = ["due_back"]
        permissions = (("can_mark_returned", "Set Book as Returned"),)

    def __str__(self):
        return self.imprint


class Profile(models.Model):
    roll_number = models.IntegerField()
    user = models.OneToOneField(User, primary_key=True,related_name='foobar')

    def __str__(self):
        return self.user.get_username()

