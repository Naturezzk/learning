# Register your models here.
from django.contrib import admin
from .models import Choice, Document
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class DocumentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['document_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('document_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['document_text']

admin.site.register(Document, DocumentAdmin)
