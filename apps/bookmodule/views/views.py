from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    # this view return index
	return render(request, 'bookmodule/index.html')

def books(request):
    return render(request, 'bookmodule/bookList.html', {'books:__getBokks()'})

def filterBooks(request):
    # this view return index
    return render(request, 'bookmodule/search.html', {})

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

    
        