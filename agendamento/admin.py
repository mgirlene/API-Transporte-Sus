from django.contrib import admin
from .models import Agendamento, Status, StatusAgendamento

admin.site.register(Agendamento)
admin.site.register(Status)
admin.site.register(StatusAgendamento)