from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

# from django.apps import apps

# myapp = apps.get_app_config('swpsdata')
# for model in myapp.get_models():
#     admin.site.register(model)

@admin.register(Donations)
@admin.register(DonationsCat)
@admin.register(Staff)
@admin.register(Voice)
@admin.register(Hundi)

class DonationsAdmin(ImportExportModelAdmin):
    pass

class DonationsCatAdmin(ImportExportModelAdmin):
    pass

class StaffCatAdmin(ImportExportModelAdmin):
    pass