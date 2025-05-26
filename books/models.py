from django.db import models


class Book(models.Model):
    GENRE = (
        ('Фантастика', 'Фантастика'),
        ('История', 'История'),
        ('Ужасы', 'Ужасы')
    )
    image = models.ImageField(upload_to='books/', verbose_name='Загрузите фото')
    title = models.CharField(max_length=100, verbose_name='Укажите название книги')
    create_at = models.DateTimeField(auto_now_add=True)
    genre = models.CharField(max_length=100, choices=GENRE, verbose_name='Укажите жанр',
                             default='История')
    author = models.CharField(max_length=100, default='Иванов Иван')
    description = models.TextField(verbose_name='Укажите описание книги')
    audio_book = models.URLField(verbose_name='Вставьте ссылку аудио книги')
    page_number = models.PositiveIntegerField(verbose_name='Укажите кол-во страниц', default=200, 
                                              null=True)
    views = models.PositiveIntegerField(
        default=0, verbose_name="Количество просмотров", null=True
    )  # Поле просмотров
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'книгу'
        verbose_name_plural = 'книги'


class Reviews(models.Model):
    books_choice = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    user_name = models.CharField(max_length=100, verbose_name='как вас зовут?')
    text = models.TextField(verbose_name='как вам книга?')

    def __str__(self):
        return f'{self.books_choice}-{self.user_name}'
    
    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'
