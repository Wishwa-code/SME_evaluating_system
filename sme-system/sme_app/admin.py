from django.contrib import admin

# Register your models here.
from .models import Employee, Styles, Daily_amounts, Daily_report

admin.site.register(Employee)
admin.site.register(Styles)
admin.site.register(Daily_amounts)
admin.site.register(Daily_report)

