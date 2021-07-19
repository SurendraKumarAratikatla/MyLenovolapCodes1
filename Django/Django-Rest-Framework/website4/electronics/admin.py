from django.contrib import admin

from .models import Laptop, Registration

admin.site.site_header = "Electronics"
admin.site.site_title = "Online Store"
admin.site.index_title = 'Welcome to online store'
admin.site.register(Laptop)
#admin.site.register(Registration)

#admin.site.unregister(Group)
#admin.site.unregister(User)
class SnippetAdmin(admin.ModelAdmin):
    #exclude = ('name',) # hiding name field also we can mention here multiple fields
    #fields = ('name',) # showing only name filed also we can mention here multiple fields
    list_display = ('email','username','date_joined','last_login','is_admin','is_staff')
    #list_filter = ('name',)
admin.site.register(Registration,SnippetAdmin)
#admin.site.register(Laptop,SnippetAdmin)
#admin.site.unregister(Group)