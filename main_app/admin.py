from django.contrib import admin

# Register your models here.
#from finch model
from.models import Finch, Feeding, Toy

#register models
admin.site.register(Finch)
admin.site.register(Feeding)
admin.site.register(Toy)