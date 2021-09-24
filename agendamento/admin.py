from django.contrib import admin
from .models import Agendamento, StatusAgendamento

admin.site.register(Agendamento)
admin.site.register(StatusAgendamento)