from django.contrib import admin
from .models import CustomUsuario, EnderecoUser
from django.contrib.auth import admin as auth_admin

admin.site.register(CustomUsuario, auth_admin.UserAdmin)
admin.site.register(EnderecoUser)