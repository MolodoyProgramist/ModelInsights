from django.db import models

class LibraryBook(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    isbn = models.CharField(max_length=50)
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ['author']  # сортировка по полю author по возрастанию
        indexes = [
            models.Index(fields=['title'], name='title_idx'),  # индекс на поле title
        ]
        constraints = [
            models.UniqueConstraint(fields=['title'], name='unique_title')  # уникальный индекс на title
        ]

    def __str__(self):
        return f"{self.title} - {self.author}"



# Create your models here.
