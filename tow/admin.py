from django.contrib import admin

# Register your models here.
from tow.models import *

admin.site.register(User)
admin.site.register(Towing)
admin.site.register(Employee)
admin.site.register(Customer)
admin.site.register(Incident)


