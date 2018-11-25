from django.contrib import admin
from home.models import Patient_Detail, Hospital, Medical_Library
from import_export.admin import ImportExportModelAdmin


admin.site.register(Patient_Detail)
admin.site.register(Hospital)


@admin.register(Medical_Library)
class PersonAdmin(ImportExportModelAdmin):
    pass