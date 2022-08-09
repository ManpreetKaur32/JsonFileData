from django.contrib import admin
from .models import *

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Address', 'Phone', 'Reviews')
    # list_display = ('image_tag','Name','Address','Phone','Reviews')
    search_fields = ('Name',)

class mydataAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Address', 'Phone', 'Reviews')
    # list_display = ('image_tag','Name','Address','Phone','Reviews')
    search_fields = ('Name',)

admin.site.register(mydata, mydataAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(JsonFile)
