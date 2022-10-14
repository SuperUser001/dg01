from django.db import models

# Create your models here.
class News(models.Model):
    #id django auto create 
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото', blank=True)  #FileField
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    
    def __str__(self): #возвращаем строковое представление объекта при запросе
        return self.title
    
    
    class Meta:
        verbose_name = 'Новость' #Наименование модели в ед.числе 
        verbose_name_plural = 'Новости' 
        ordering = ['created_at', 'title'] #сортировка