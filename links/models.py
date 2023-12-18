from django.db import models
from django.utils.text import slugify

# Create your models here.
class Link(models.Model):
    name = models.CharField(max_length=100, unique=True)
    url = models.URLField(unique=True)
    slug = models.SlugField(unique=True, blank=True)
    clicks = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.name} - {self.url}"
    
    def click(self):
        self.clicks += 1
        self.save(update_fields=["clicks"])
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)