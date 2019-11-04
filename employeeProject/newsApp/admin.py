from django.contrib import admin
from newsApp.models import employee

class employeeAdmin(admin.ModelAdmin):
	list_display=['eno','ename','esal','eaddress']

# Register your models here.
admin.site.register(employee,employeeAdmin)
