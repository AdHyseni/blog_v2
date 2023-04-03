from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class Autori(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pen_name = models.CharField(max_length=50, null=False)

    def __str__(self) -> str:
        return f'{self.pen_name}'



class Post(models.Model):
    autori = models.ForeignKey(Autori, on_delete=models.DO_NOTHING)
    titulli = models.CharField(max_length=150, null=False)
    tekst = models.TextField(max_length=300, null=False)
    foto = models.ImageField(upload_to='post',null=True,blank=True)
    slug = models.SlugField(blank=True)
    time = models.DateTimeField(auto_created=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.titulli}')
        super(Post, self).save(*args, **kwargs)


    def __str__(self) -> str:
        return f'{self.titulli}'