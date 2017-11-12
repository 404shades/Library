from django.db import models
from django.db.models.signals import pre_save,post_save
from .utils import unique_slug_generator

class Books(models.Model):
    Book_Title      = models.CharField(max_length=250)
    ISBN            = models.CharField(max_length=250)
    page_amount     = models.IntegerField()
    timestamp       = models.DateTimeField(auto_now_add=True)
    LendingDate     = models.DateTimeField(auto_now=True)
    slug            = models.SlugField(blank=True,null=True)
    def __str__(self):
        return self.Book_Title

    @property
    def title(self):
        return self.Book_Title

    def getBookTitle(self):
        return self.Book_Title

def rl_pre_save_receiver(sender,instance,**kwargs):
    print('Saving....')
    instance.Book_Title = instance.Book_Title.capitalize()
    print(instance.timestamp)
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
        instance.save()


pre_save.connect(rl_pre_save_receiver,sender=Books)