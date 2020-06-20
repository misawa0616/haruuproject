from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import HaruuUser, Application, EmailConfirm


class HaruuAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password', 'application')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'token', 'created_at', 'updated_at')
    fieldsets = [
        (None, {'fields': ('email', 'token')}),
    ]


class EmailConfirmAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'token', 'created_at', 'haruu_user')
    fieldsets = [
        (None, {'fields': ('email', 'token')}),
    ]


admin.site.register(HaruuUser, HaruuAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(EmailConfirm, EmailConfirmAdmin)
