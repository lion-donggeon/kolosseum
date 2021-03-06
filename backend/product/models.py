from io import BytesIO
from PIL import Image

from django.core.files import File
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    creator = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    image = models.ImageField(upload_to='image/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='thumbnail/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'

    """
    로컬
    """
    # def get_image(self):
    #     if self.image:
    #         return 'http://127.0.0.1:8000' + self.image.url
    #     return ''
    
    # def get_thumbnail(self):
    #     if self.thumbnail:
    #         image = self.image.url.split('/')[3]
    #         thumbnai = self.thumbnail.url.split('/')[3]

    #         if( image == thumbnai ):
    #             return 'http://127.0.0.1:8000' + self.thumbnail.url
    #         else:
    #             self.thumbnail = self.make_thumbnail(self.image)
    #             self.save()

    #             return 'http://127.0.0.1:8000' + self.thumbnail.url
            
    #     else:
    #         if self.image:
    #             self.thumbnail = self.make_thumbnail(self.image)
    #             self.save()

    #             return 'http://127.0.0.1:8000' + self.thumbnail.url
    #         else:
    #             return ''

    """
    운영
    """
    def get_image(self):
        if self.image:
            return 'http://15.165.73.177' + self.image.url
        return ''
    
    def get_thumbnail(self):
        if self.thumbnail:
            image = self.image.url.split('/')[3]
            thumbnai = self.thumbnail.url.split('/')[3]

            if( image == thumbnai ):
                return 'http://15.165.73.177' + self.thumbnail.url
            else:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://15.165.73.177' + self.thumbnail.url
            
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://15.165.73.177' + self.thumbnail.url
            else:
                return ''
    


    """
    공용
    """

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img = img.convert('RGB')
        img.thumbnail(size)

        name = image.name.split("/")[1]

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)
        thumbnail = File(thumb_io, name=name)

        return thumbnail