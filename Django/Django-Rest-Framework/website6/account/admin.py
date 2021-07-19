from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Account


class AccountAdmin(UserAdmin):
    model = Account
    list_display = ('email','username','date_joined','last_login','is_admin','is_staff')
    search_fields = ('email','username')
    ordering = ('email',)
    readonly_fields = ('id','date_joined','last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    # fieldsets = (
    #     (None, {'fields':('email','username','password')}),
    #     ('Permissions', {'fields':('is_staff','is_active','groups','user_permissions',)})
    # )
    #
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields' : ('email','username','date_joined','last_login','is_admin','is_staff')
    #     })
    # )

admin.site.register(Account,AccountAdmin)
