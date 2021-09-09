from django.contrib import admin
from .models import CustomUsuario
from django.contrib.auth import admin as auth_admin

admin.site.register(CustomUsuario, auth_admin.UserAdmin)