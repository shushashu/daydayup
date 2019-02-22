from django.contrib import admin

# Register your models here.
from .models import WeixinUser

admin_site = admin.site

admin_site.register(model_or_iterable=WeixinUser)
