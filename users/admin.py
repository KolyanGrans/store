from django.contrib import admin
from .models import User
from products.admin import BasketAdminInline
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = (BasketAdminInline,)
