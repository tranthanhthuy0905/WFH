from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accountTracking.models import Account

class accountAdmin(UserAdmin):
    list_display = ('username', 'email', 'created_on', 'last_login', 'is_admin')
    search_fields = ('username', 'email',)
    readonly_fields = ('created_on', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, accountAdmin)

