from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=100, verbose_name='URL', unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', verbose_name='Родительская категория')
    class Meta:
        verbose_name = 'Каткгория'
        verbose_name_plural = 'Категории'
        ordering = ['name']
    def __str__(self):
        return self.name
    
class Product(models.Model):
    class AlcoholType(models.TextChoices):
        VODKA = 'vodka', ('Водка')
        WHISKEY = 'whiskey', ('Виски')
        COGNAC = 'cognac', ('Коньяк')
        WINE = 'wine', ('Вино')
        BEER = 'beer', ('Пиво')
        CHAMPAGNE = 'champagne', ('Шампанское')
        LIQUEUR = 'liqueur', ('Ликер')
        TEQUILA = 'tequila', ('Текила')
        RUM = 'rum', ('Ром')
        GIN = 'gin', ('Джин')
        OTHER = 'other', ('Другое')
    name = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(max_length=200, verbose_name='URL')
    image = models.ImageField(upload_to='products/', blank=True, verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категория')
    alcohol_type = models.CharField(max_length=20, choices=AlcoholType.choices, verbose_name='Тип алкоголя')
    brand = models.CharField(max_length=100, verbose_name='Бренд')
    country = models.CharField(max_length=100, verbose_name='Страна производства')
    volume = models.DecimalField(max_digits=5, decimal_places=2, help_text='В литрах', verbose_name='Объем')
    strength = models.DecimalField(max_digits=4, decimal_places=1,help_text='в процентах', verbose_name='Крепость')
    description = models.TextField(max_length=300, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    stock = models.PositiveIntegerField(verbose_name='Количество на складе')
    available = models.BooleanField(default=True, verbose_name='Доступен')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    class Meta:
        ordering = ['-created']
        indexes = [models.Index(fields=['id', 'slug']),]
        verbose_name = ('Продукт')
        verbose_name_plural = ('Продукты')
    def __str__(self):
        return f"{self.brand}{self.name}({self.volume}л, {self.strength}%)"
