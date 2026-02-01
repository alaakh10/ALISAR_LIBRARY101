from django.contrib import admin
from .models import Category, Author, Book, Admin

# إعداد التصنيفات في Admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category_type']
    list_filter = ['category_type']
    search_fields = ['name']
    ordering = ['name']

# إعداد المؤلفين في Admin  
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    ordering = ['name']

# إعداد الكتب في Admin
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'created_at']
    list_filter = ['category']  
    search_fields = ['title', 'author__name', 'category__name']  
    ordering = ['-created_at']

# إعداد الأدمنز في Admin
class AdminAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'role', 'created_at']
    list_filter = ['role']
    search_fields = ['username', 'email']
    ordering = ['-created_at']

# تسجيل الموديلز مع الإعدادات
admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Admin, AdminAdmin)