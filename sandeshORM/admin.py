from django.contrib import admin

# Register your models here.
from .models import Reporter, Article, Owner, Car, Owner1, Car1, Driver, Car2


admin.site.register(Reporter)
admin.site.register(Article)
admin.site.register(Owner)
admin.site.register(Car)
admin.site.register(Owner1)
admin.site.register(Car1)
admin.site.register(Driver)
admin.site.register(Car2)
