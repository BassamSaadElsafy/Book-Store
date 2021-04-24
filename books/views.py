from django.shortcuts import render, redirect
from .forms import BookForm

from .models import Book
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

@login_required    #(login_url="/login")
def index(request):
    
    books = Book.objects.all()
    return render(request, "books/index.html", {
        "books" : books
    })

@permission_required(['books.add_book'], raise_exception=True)
def create(request):
    form = BookForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("index")

    return render(request, "books/create.html", {
        "form" : form,
    })

@permission_required(['books.change_book'], raise_exception=True)
def edit(request, id):

    book = Book.objects.get(pk=id)

    form = BookForm(request.POST or None, instance=book)

    if form.is_valid():
        form.save()
        return redirect("index")

    return render(request, "books/edit.html", {
        "form" : form,
        "book" : book
    })


def show(request, id):

    book = Book.objects.get(pk=id)
    return render(request, "books/show.html", {
        "book" : book
    })


def destroy(request, id):

    book = Book.objects.get(pk=id)
    book.delete()
    return redirect("index")
