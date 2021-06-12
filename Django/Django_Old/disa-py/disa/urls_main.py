"""disa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from disa.views import *
from django.contrib.auth.decorators import login_required
from member.views import CustomEmail, CustomSms, Reports

'''from adminplus.sites import AdminSitePlus

admin.site = AdminSitePlus()
admin.autodiscover()'''

urlpatterns = [

    url(r'^py-admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name='landing.html'),
        name='landing'),
    url(r'^home/$', HomeView.as_view(), name='home'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^organisation/$', OrganisationView.as_view(), name='organisation'),
    url(r'^members/$', login_required(TemplateView.as_view(
        template_name="members.html")), name='members'),
    url(r'^member/(?P<mid>[0-9A-Za-z-]+)/$', MemberView.as_view(),
        name='member-view'),
    url(r'^member/$', UserProfileView.as_view(),
        name='profile-view'),
    url(r'^members-search/$', MSearchView.as_view(), name='members-search'),
    url(r'^seva-search/$', SSearchView.as_view(), name='seva-search'),
    url(r'^reports/templates/$', ReportSevaTemplates.as_view(),
        name='reports_seva_templates'),
    url(r'^reports/sevas/$', ReportsSeva.as_view(), name='reports_seva'),
    url(r'^seva-cat/$', SevaCategoryView.as_view(), name='seva-cat'),
    url(r'^seva-cat-search/$', SevaCategorySearch.as_view(),
        name='seva-cat-search'),
    url(r'^reports/location/$', login_required(TemplateView.as_view(
        template_name="reports_location.html")), name='reports_location'),
    url(r'^loc-search/$', LocationSearch.as_view(), name='loc-search'),
    url(r'^reports/month/$', ReportsMonthly.as_view(), name='reports_monthly'),
    url(r'^seva-month-search/$', SevaMonthlySearch.as_view(),
        name='seva-month-search'),
    url(r'^reports/awardee/$', ReportsAwardee.as_view(),
        name='reports_awardee'),
    url(r'^reports/search-awardee/$', AwardeeSearch.as_view(),
        name='search-awardee'),
    url(r'^member/edit/(?P<m_id>[0-9A-Za-z-]+)/$', MemberEditView.as_view(),
        name='member-edit'),
    url(r'^member/upload/(?P<m_id>[0-9A-Za-z-]+)/$', MemberImageUpload.as_view(),
        name='member-image-upload'),
    url(r'^add/member/$', MemberAdd.as_view(), name='add-member'),
    url(r'^sevas/(?P<s_id>[0-9A-Za-z-]+)/edit$', SevaEditView.as_view(),
        name='edit-seva'),
    url(r'^add/(?P<m_id>[0-9A-Za-z-]+)/seva/$', SevaAdd.as_view(), name='add-seva'),
    url(r'^member/(?P<m_id>[0-9A-Za-z-]+)/address/$', MemberAddress.as_view(),
        name='member-address'),
    url(r'^member/(?P<m_id>[0-9A-Za-z-]+)/address/edit/(?P<aid>[0-9A-Za-z-]+)/$',
        MemberAddressEdit.as_view(), name='member-address-edit'),
    url(r'^organisation/edit/(?P<org_id>[0-9A-Za-z-]+)/$',
        OrganisationEdit.as_view(), name='edit_org'),
    url(r'^export-loc-search/$', ExportLocationReports.as_view(), name='export-loc-search'),
    url(r'^export-seva-search/$', ExportSevaSearch.as_view(), name='export-seva-search'),
    url(r'^export-maasam-seva-search/$', ExportMasamSevaSearch.as_view(), name='export-maasam-seva-search'),
    url(r'^export-awardee/$', ExportAwardee.as_view(), name='export-awardee'),

    url(r'^reports/lunar/$', ReportsMaasam.as_view(), name='reports_maasam'),
    url(r'^seva-maasam-search/$', SevaMaasamSearch.as_view(),
        name='seva-maasam-search'),
    url(r'^email/$', CustomEmail.as_view(), name='email'),
    url(r'^sms/$', CustomSms.as_view(), name='sms'),
    url(r'^add/user/$', UserAdd.as_view(), name='add-user'),
    url(r'^edit/user/(?P<user_id>[0-9]+)/$', UserEdit.as_view(), name='edit-user'),
    url(r'^user/access/$', MemberAccess.as_view(), name='user-access'),
    url(r'^import-group/$', ImportGroup.as_view(), name='import-group'),
    url(r'^group-view/$', GroupView.as_view(), name='group-view'),

    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^medicalprofile-view/(?P<m_id>[0-9A-Za-z-]+)/$', MedicalProfileView.as_view(), name='medicalprofile'),
    url(r'^add/membership/(?P<m_id>[0-9A-Za-z-]+)/$', MembershipAdd.as_view(), name='add-membership'),
    url(r'^add/relationship/(?P<m_id>[0-9A-Za-z-]+)/$', AddRelationship.as_view(), name='add-relationship'),
    url(r'^relationship-search/$', RelationSearchView.as_view(), name='relationship-search'),
    url(r'^membership/(?P<m_id>[0-9A-Za-z-]+)/$', MembershipView.as_view(), name='membership-view'),
]
