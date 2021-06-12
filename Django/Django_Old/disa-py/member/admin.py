from django.contrib import admin

# Register your models here.
from models import *
from django.contrib.admin import ModelAdmin
from django.db.models.fields import Field
from django.contrib.admin import SimpleListFilter

'''#from assign.disa-py.disa.admin_site import custom_admin_site
class country(SimpleListFilter):
    title = 'name' # or use _('country') for translated title
    parameter_name = 'name'

    def lookups(self, request, model_admin):

        list_of_countries = []
        queryset = Organisation.objects.all()
        for countries in queryset:
            list_of_countries.append(self.id)
        return sorted(list_of_countries, key=lambda tp: tp[1])

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(organisations_id=self.value())
        return str(queryset)


class CityAdmin(ModelAdmin):
    list_filter = (country, )



@admin.register(Author, Reader, Editor, site=custom_admin_site)
class PersonAdmin(admin.ModelAdmin):
    pass
'''

'''class AddressAdmin(admin.ModelAdmin):
    list_display = ('mid','address','city','district','state','country','pin','phone')
    #list_display = ('full_address', 'pin')
    ordering = ['country']
    actions = [ 'mark_seen']
    def mark_seen(self, request, queryset):
        queryset.update(status='p')
    mark_seen.short_description = "Mark seen"



def my_view(request, *args, **kwargs):
    user1 = Seva.objects.values_list('sevaday', flat=True)[0];
    return u'%s' % (user1)

admin.site.register_view('somepath', view=my_view)'''

admin.site.register(Address, AddressAdmin)
admin.site.register(Awardee, AwardeeAdmin)
admin.site.register(LunarDate, LunarAdmin)
admin.site.register(Member, MembersAdmin)
admin.site.register(NakshatramRasiPadamData, NakshatramRasiPadamDataAdmin)
admin.site.register(Seva, SevasAdmin)
admin.site.register(DonationKind, DonationKindAdmin)
admin.site.register(DonationCash, DonationCashAdmin)
admin.site.register(DonationAsset, DonationAssetAdmin)
admin.site.register(DonationService, DonationServiceAdmin)

admin.site.register(MaasamType, commonAdmin)
admin.site.register(NakshatramType, commonAdmin)
# admin.site.register(OauthAccesstoken, commonAdmin)
# admin.site.register(OauthAuthCode, commonAdmin)
# admin.site.register(OauthRefreshToken, commonAdmin)
admin.site.register(Organisation, commonAdmin)
admin.site.register(Profile, commonAdmin)
admin.site.register(SVExtra, commonAdmin)
admin.site.register(PadamType, commonAdmin)
admin.site.register(PakshamType, commonAdmin)
admin.site.register(RasiType, commonAdmin)
admin.site.register(SequenceNumber, commonAdmin)
admin.site.register(SevaAddress, commonAdmin)
admin.site.register(SevaCategory, commonAdmin)
admin.site.register(Tag, commonAdmin)
admin.site.register(TithiType, commonAdmin)
admin.site.register(MedicalProfile, MedicalProfileAdmin)
admin.site.register(StaffProfile, StaffProfileAdmin)
admin.site.register(User, commonAdmin)

admin.site.register(Transaction)
admin.site.register(SevasAddress, SevasAddressAdmin)

admin.site.register(AssetLand, AssetLandAdmin)
admin.site.register(AssetBuilding, AssetBuildingAdmin)
admin.site.register(AssetEquipment, AssetEquipmentAdmin)

admin.site.register(Trustee, TrusteeAdmin)
admin.site.register(Honorary, commonAdmin)
admin.site.register(Complimentary, commonAdmin)
admin.site.register(Relatives, RelativesAdmin)

admin.site.register(Duration)
