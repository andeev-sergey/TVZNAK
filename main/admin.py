from django.contrib import admin
from .models import *
# Register your models here.


from django.contrib.auth.models import Group

admin.site.unregister(Group)

# Register your models here.
admin.site.index_title = 'Администрирование сайта'
admin.site.site_title = 'TVZNAK'
admin.site.site_header = 'TVZNAK'


class RequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'time', 'status')
    list_filter = ('status',)


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('time', 'status')
    list_filter = ('status',)


admin.site.register(Request, RequestAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(Contact)
admin.site.register(Subscription)
admin.site.register(TvBox)
admin.site.register(Channel)