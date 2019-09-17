from django.db import models

class Child(models.Model):
    name= models.CharField(max_length=100, verbose_name="Child's First Name and Last Name")
    weight= models.DecimalField(max_digits=5, decimal_places=2,)

    class Meta:
        
        verbose_name_plural= 'children'

    def __str__(self):
        return self.name

