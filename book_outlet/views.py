from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.db.models import Avg

# Import model for query
from .models import Book

# Create your views here.


def index(request):
    # By chaining order by, it adds order in SQL query
    # a minus can be used to order in desc order
    books = Book.objects.all().order_by("-title")
    # Generate using Python other values
    total_books = books.count()
    avg_rating = books.aggregate(Avg("rating"))

    return render(request, "book_outlet/index.html", {
        "books": books,
        "total_books": total_books,
        "average_rating": avg_rating["rating__avg"],
    })


def book_detail(request, slug):
    # Search for book
    # try:
    #     book = Book.objects.get(pk=id)
    # If not found, raise 404
    # except:
    #     raise Http404

    # The above can be replaced with
    book = get_object_or_404(Book, slug=slug)

    # Return
    return render(request, "book_outlet/book_detail.html", {
        "book": book,
    })
