from django.contrib import admin
from .models import Book, ISBN, Category, Tag
from .forms import BookForm

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    form = BookForm                  #to apply form validation on admin panel
    list_display= ("title", "description", "user", "isbn")
    list_filter = ("categories","user")
    search_fields = ("title", "description")
    readonly_fields = ("isbn", )

class BookInline(admin.StackedInline):
    model   = Book
    max_num = 3
    extra   = 1
    
class TagAdmin(admin.ModelAdmin):
    inlines = [BookInline]

admin.site.register(Book, BookAdmin)
admin.site.register(ISBN)
admin.site.register(Category)
admin.site.register(Tag, TagAdmin)
