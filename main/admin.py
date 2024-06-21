from django.contrib import admin
from .models import Trainers
from .models import Athletes
from .models import Sports
from .models import News
from .models import Contact
class TrainersAdmin(admin.ModelAdmin):
    list_display = ['name']
    
admin.site.register(Trainers, TrainersAdmin)

class AthletesAdmin(admin.ModelAdmin):
    list_display = ['name']
    
admin.site.register(Athletes, AthletesAdmin)

class SportsAdmin(admin.ModelAdmin):
    list_display = ['name']
    
admin.site.register(Sports, SportsAdmin)

class NewsAdmin(admin.ModelAdmin):
    list_display = ['name']
    
admin.site.register(News, NewsAdmin) 

class ContactAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'age', 'sport', 'phone', 'email']

admin.site.register(Contact, ContactAdmin)
