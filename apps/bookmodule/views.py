from django.shortcuts import render, redirect
from .models import Book

def index(request):
    # this view return index
	return render(request, 'bookmodule/index.html')

def books(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/bookList.html', {'books': books})

def book(request, bId): # read/sgiw/disply
    obj = Book.objects.get(id = bId)
    return render(request, 'bookmodule/book.html', {'book':obj})

# Create your views here.
def index(request):
    # this view return index
	return render(request, 'bookmodule/index.html')

def books(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/bookList.html', {'books': books})

def contactPage(request):
    # this view return index
	return render(request, 'bookmodule/contactPage.html')

def books(request):
    return render(request, 'bookmodule/bookList.html', {'books:__getBokks()'})


def books(request):
    return render(request, 'bookmodule/bookList.html', {'books': books})

def books(request):
    return render(request, 'bookmodule/bookList.html')

def filterBooks(request):
    # this view return index
    
    
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        
        selected = request.POST.get('selectedgenre')
        
        mybook1 = Book.objects.filter(title__icontains='or')
        mybook2 = book.filter(price__lte = 100).exclude(author_icontains = 'Saad')
        mybook1.save()
        mybook2.save()
        
        print(f"selected thing = {selected}")
        # now filter
        books = __getBooks()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower(): contained = True
            if not contained and isAuthor and string in item['author'].lower(): contained = True
            if contained: newBooks.append(item)       
        return render(request, 'bookmodule/bookList.html', {'books':newBooks})
    return render(request, 'bookmodule/index.html', {})

def book(request, bId):

    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
    book2 = {'id':56788765, 'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    
    targetBook = None
    if book1['id'] == bId: targetBook = book1
    if book2['id'] == bId: targetBook = book2
    
    if targetBook == None: return redirect('/books')

    context = {'book':targetBook} # book is the variable name accessible by template
    return render(request, 'bookmodule/book.html', context)

def __getBooks():
    books = []
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
    books.append(book1)
    book2 = {'id':56788765, 'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    books.append(book2)
    
    return books

    
        