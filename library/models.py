from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Manager for Admin model
class AdminManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

# جدول التصنيفات 
class Category(models.Model):
    category_id = models.AutoField(primary_key=True, verbose_name="رقم التصنيف")
    
    CATEGORY_CHOICES = [
        ('education', 'تعليمي'),
        ('novels', 'روايات أدبية'),
        ('self', 'تطوير الذات'),
        ('history', 'تاريخية'),
        ('translated', 'عالمية مترجمة'),
        ('religious', 'كتب دينية'),
    ]
    
    name = models.CharField(max_length=100, verbose_name="اسم التصنيف")
    category_type = models.CharField(max_length=50, choices=CATEGORY_CHOICES, verbose_name="نوع التصنيف")
    description = models.TextField(blank=True, null=True, verbose_name="الوصف")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإضافة")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "تصنيف"
        verbose_name_plural = "التصنيفات"

# جدول المؤلفين
class Author(models.Model):
    author_id = models.AutoField(primary_key=True, verbose_name="رقم المؤلف")
    name = models.CharField(max_length=100, verbose_name="اسم المؤلف")
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "مؤلف"
        verbose_name_plural = "المؤلفين"

# جدول الكتب
class Book(models.Model):
    book_id = models.AutoField(primary_key=True, verbose_name="رقم الكتاب")
    title = models.CharField(max_length=200, verbose_name="عنوان الكتاب")
    
    author = models.ForeignKey(
        Author, 
        on_delete=models.CASCADE, 
        verbose_name="المؤلف",
        null=True,
        blank=True
    )
    
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, 
        verbose_name="التصنيف"
    )
    
    description = models.TextField(verbose_name="الوصف", blank=True)
    pdf_file = models.FileField(upload_to='books/', verbose_name="ملف الكتاب")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإضافة")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "كتاب"
        verbose_name_plural = "الكتب"


# جدول الأدمنز
class Admin(AbstractBaseUser):
    admin_id = models.AutoField(primary_key=True, verbose_name="رقم المدير")
    username = models.CharField(max_length=50, unique=True, verbose_name="اسم المستخدم")
    email = models.EmailField(unique=True, verbose_name="البريد الإلكتروني")
    password = models.CharField(max_length=255, verbose_name="كلمة المرور")
    full_name = models.CharField(max_length=100, verbose_name="الاسم الكامل")
    role = models.CharField(max_length=20, choices=[
        ('super_admin', 'مدير عام'),
        ('library_staff', 'موظف مكتبة')
    ], default='library_staff', verbose_name="الدور")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")

    objects = AdminManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "مدير"
        verbose_name_plural = "المدراء"
