from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    """Create entry fields for Product model."""

    title = models.CharField(max_length=50)
    url = models.URLField()
    pub_date = models.DateTimeField()
    votes_total = models.IntegerField(default=1)
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    body = models.TextField(max_length=500)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def date_view(self):
        self.pub_date.strftime('%b %e %Y')

    def summary(self):
        return self.body[:100]
