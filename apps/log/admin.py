from django.contrib import admin
from .models import TemporaryLogin,FormalLogin
# Register your models here.

admin.site.register([TemporaryLogin,FormalLogin])
