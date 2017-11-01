from django.db import models

class Books(models.Model):
    Book_Title = models.CharField(max_length=250)
    ISBN = models.CharField(max_length=250)
    lend_from = models.DateField(null=True, blank=True)
    page_amount = models.IntegerField()

    def __str__(self):
        return self.Book_Title
