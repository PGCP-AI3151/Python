from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponse
from .models import Book
#
# books = [
#     {'title': 'Python Learning', 'author': 'abc', 'price': 10},
#     {'title': 'ML With Python', 'author': 'xyz', 'price': 50},
#     {'title': 'Java Learning', 'author': 'efg', 'price': 25},
# ]

def home(request):
    context = {'books': Book.objects.all()}
    #return HttpResponse('<h3> Hello World </h3>')
    return render(request, 'book/index.html', context)

def about(request):
    # return HttpResponse('<h3> About </h3>')
    return render(request, 'book/about.html', {'title': 'About Us'})

def book_details(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book/book_details.html', context={'book': book})