from django.contrib import admin
from .models import UserProfile, Item
# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'description',
                    'price',
                    'discount_price',
                    'category',
                    'slug',
                    'image_tag'
                    )
    

                                                                                        

admin.site.register(UserProfile)
admin.site.register(Item, ItemAdmin)