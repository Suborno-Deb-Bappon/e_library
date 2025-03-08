from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class EBook(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author)
    publication_date = models.DateField()
    description = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    file = models.FileField(upload_to='ebooks/')
    licenses = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title

class Borrowing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ebook = models.ForeignKey(EBook, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()  # Required, set to 14 days from borrow_date
    return_date = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk and not self.due_date:  # Only set on creation
            self.due_date = timezone.now() + timezone.timedelta(days=14)
        super().save(*args, **kwargs)

    def is_overdue(self):
        return self.return_date is None and timezone.now() > self.due_date

    def __str__(self):
        return f"{self.user.username} - {self.ebook.title}"

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ebook = models.ForeignKey(EBook, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'ebook')

    def __str__(self):
        return f"{self.user.username} - {self.ebook.title}: {self.rating}"