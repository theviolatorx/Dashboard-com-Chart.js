from django.contrib import admin

from .models import Produto, Venda, Vendedor

# Register your models here.

admin.site.register(Venda)
admin.site.register(Vendedor)
admin.site.register(Produto)
