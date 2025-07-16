from django.contrib import admin
from pomo.models import Pomo

# Register your models here.
@admin.register(Pomo)
class PomoAdmin(admin.ModelAdmin):
    list_display = ('id', 'time', 'created')