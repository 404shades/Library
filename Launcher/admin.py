from django.contrib import admin
from .models import Books,Subject,BookInstance
# Register your models here.
admin.site.register(Books)
admin.site.register(Subject)


class BookInstanceInline(admin.TabularInline):
    model = BookInstance


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('status','due_back','id','book','borrower')
    list_filter = ('status','due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )