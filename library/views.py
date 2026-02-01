from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q  
import json
from .models import Book, Category, Author

def religious_books(request):
    """عرض الكتب الدينية"""
    books = Book.objects.filter(category__category_type='religious')
    return render(request, 'library/religious_books.html', {
        'books': books,
        'title': 'الكتب الدينية'
    })

def index(request):
    """الصفحة الرئيسية"""
    return render(request, 'library/index.html')

def education_books(request):
    """عرض الكتب التعليمية"""
    books = Book.objects.filter(category__category_type='education')
    return render(request, 'library/education.html', {'books': books})

def novels_books(request):
    """عرض الروايات"""
    books = Book.objects.filter(category__category_type='novels')
    return render(request, 'library/novels.html', {'books': books})

def self_development_books(request):
    """عرض كتب التنمية الذاتية"""
    books = Book.objects.filter(category__category_type='self')
    return render(request, 'library/self_development.html', {'books': books})

def history_books(request):
    """عرض الكتب التاريخية"""
    books = Book.objects.filter(category__category_type='history')
    return render(request, 'library/history.html', {'books': books})

def translated_books(request):
    """عرض الكتب المترجمة"""
    books = Book.objects.filter(category__category_type='translated')
    return render(request, 'library/translated.html', {'books': books})

def search_books(request):
    query = request.GET.get('q', '').strip()
    
    if query:
        books = Book.objects.filter(
            Q(title__icontains=query) |
            Q(author__name__icontains=query) |
            Q(description__icontains=query) |
            Q(category__name__icontains=query)
        ).distinct()
    else:
        books = Book.objects.all()[:12]
    
    context = {
        'query': query,
        'books': books,
    }
    
    return render(request, 'library/search_results.html', context)


def book_detail(request, book_id):
    """عرض تفاصيل كتاب معين"""
    try:
        book = Book.objects.select_related('author', 'category').get(pk=book_id)
        related_books = Book.objects.filter(
            category=book.category
        ).exclude(pk=book_id)[:4]  
        
        context = {
            'book': book,
            'related_books': related_books
        }
        return render(request, 'library/book_detail.html', context)
    except Book.DoesNotExist:
        return render(request, 'library/404.html', {'message': 'الكتاب غير موجود'})