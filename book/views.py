from django.shortcuts import render
from book.models import Book
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')


def register(request):
    return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')

@login_required()
def books(request):
    if request.method == 'POST':
        search = request.POST['search']
        books = Book.objects.filter(name__icontains=search) | Book.objects.filter(author__first_name__icontains=search)
        if books:
            return render(request, 'books.html', {'books': books, 'value': search, "massage": 'Succesfully'})
        else:
            return render(request, 'books.html', {"massage": 'not found'})
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})

def book_detail(request, slug):
    book = Book.objacts.get(slug=slug)
    if book:
        return render(request, 'book_detail.html', {'book': book, "message": 'Succesfully'})
    else:
        return render(request, 'book_detail.html', {"message": 'Not found'})
