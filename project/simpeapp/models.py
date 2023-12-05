from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name.title()


class News(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
    )
    text = models.TextField()
    NEWS = 'NW'
    ARTICLE = 'AR'
    CATEGORY_CHOICES = (
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья'),
    )
    categoryType = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=ARTICLE)
    dateCreation = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        to='Author',
        on_delete=models.CASCADE,
        related_name='products',
    )

    def __str__(self):
        return f'{self.name.title()}...: {self.text}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class PostCategory(models.Model):
    postThrough = models.ForeignKey(News, on_delete=models.CASCADE)
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)


class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name.title()
