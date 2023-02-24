from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
# Register your models here.

# collection
admin.site.register(Items)
admin.site.register(collection)
admin.site.register(Userr)
admin.site.register(Bids)
admin.site.register(Question)
