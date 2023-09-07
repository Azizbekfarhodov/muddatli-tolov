from django.contrib import admin

# Register your models here.

from .models import Product

class ProductAdmin(admin.ModelAdmin):
     list_display = ("narx", "oldindan_tolov", "ustama", "muddat", "sana", "get_divade")
     list_filter = ("sana",)
     search_fields = ("sana",)
     list_editable = ("oldindan_tolov", "ustama", "muddat", "sana")
     list_per_page = 10

admin.site.register(Product, ProductAdmin)