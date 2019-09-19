from django.db import models
from django.conf import settings
from django.shortcuts import reverse
CATEGORY_CHOICE = (

)


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(max_length=50,
                                          blank=True,
                                          null=True)
    one_click_purchasing = models.BooleanField(default=False)


    def __str__(self):
        return self.user.username
        
class Item(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICE,
                                max_length=5)
    slug= models.SlugField()
    image= models.ImageField(null = True,
                            blank = True,
                            upload_to = "images/")

    def __str__(self):
        return self.title
    
    def image_tag(self):
        if self.image:
            return self.image.url
        else :
            return 'No Image Found'
    image_tag.short_description = 'Image'

    def get_absolute_url(self):
        return reverse('item_detail', kwargs={
            'slug': self.slug
        })



