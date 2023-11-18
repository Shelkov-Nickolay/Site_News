from django.db import models


class News(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
    )
    text = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='products',
    )
    author = models.ForeignKey(
        to='Author',
        on_delete=models.CASCADE,
        related_name='products',
    )

    def __str__(self):
        return f'{self.name.title()}...: {self.text}'


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True) 

    def __str__(self):
        return self.name.title()


class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name.title()
