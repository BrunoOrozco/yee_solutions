from import_export.admin import ImportExportModelAdmin


from users.models import Vendedores
from django.contrib import admin


@admin.register(Vendedores)
class ProfileAdmin(ImportExportModelAdmin):
    list_display = ('user', 'lider', 'region', 'created')

    verbose_name = "Vendedor"