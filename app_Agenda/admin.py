from django.contrib import admin
from .models import Agenda, Agenda_Institucional

@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    pass

@admin.register(Agenda_Institucional)
class Agenda_InstitucionalAdmin(admin.ModelAdmin):
    pass