from django.contrib import admin
from .models import Addpoll
# Register your models here.

@admin.register(Addpoll)
class AddpollAdmin(admin.ModelAdmin):
    list_display=['id','user','question','first_c','second_c','third_c','fourth_c']