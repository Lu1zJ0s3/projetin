from django.contrib import admin
from apps.core.models import veiculos

class veiculosAdmin(admin.ModelAdmin):
    list_display="nome","cor","montadora"

admin.site.register(veiculos,veiculosAdmin)