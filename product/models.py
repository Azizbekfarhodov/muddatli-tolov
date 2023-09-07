from django.db import models

# Create your models here.

class Product(models.Model):
     narx = models.IntegerField()
     oldindan_tolov = models.IntegerField()
     ustama = models.IntegerField()
     muddat = models.IntegerField()
     sana = models.DateField() 

     def __str__(self):
          return f"{self.narx} {self.oldindan_tolov} {self.ustama} {self.muddat} {self.sana}"
     
     class Meta:
          verbose_name = "Mahsulot"
          verbose_name_plural = "Mahsulotlar"
          ordering = ["-sana"]

     # get divade product price add ustama and oldindan_tolov
     def get_divade(self):
          return ((self.narx - self.oldindan_tolov) + (self.ustama * self.muddat)) / self.muddat 