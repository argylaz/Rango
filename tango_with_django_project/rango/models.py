from django.db import models
from django.template.defaultfilters import slugify

# Category model
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    # Overwriting save to automatically create a slug
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs) # Call the real save() method

    # Just fixing the plural of category
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
# Page model
class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title