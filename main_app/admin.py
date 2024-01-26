from django.contrib import admin

# Register your models here.
#from finch model
from.models import Finch, Feeding

#register models
admin.site.register(Finch)
admin.site.register(Feeding)
