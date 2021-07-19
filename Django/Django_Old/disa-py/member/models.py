# # This is an auto-generated Django model module.
# # You'll have to do the following manually to clean this up:
# #   * Rearrange models' order
# #   * Make sure each model has one field with primary_key=True
# #   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# # Feel free to rename the models, but don't rename db_table values or field names.
# #
# # Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# # into your database.
# from __future__ import unicode_literals
# from django.contrib import admin
# from django.db import models
# from django.utils.html import format_html
# from django.contrib.admin import DateFieldListFilter
# from django.db.models import Q, Lookup
# from django.contrib.admin import SimpleListFilter
# from django import forms
# from daterange_filter.filter import DateRangeFilter
# from django.utils import timezone
# import datetime
# from member.forms import MemberForm
# from member.forms import *
# from django.forms import modelform_factory
# from import_export.admin import ExportMixin
# import uuid
# from member.sms import send_SMS
# from member.email import sendmail
# from disa.middleware.current_user import get_current_user
# from django.contrib.auth.models import User as DjangoUser
# from django.template.loader import get_template
# from django.template import Context
# from django.db import connection
# from django.template.loader import render_to_string
# from django.contrib.auth import get_user_model
# from django.contrib.auth.models import Group, Permission
# from django.contrib.auth.models import BaseUserManager, PermissionsMixin
# from django.contrib.auth.hashers import check_password, make_password
#
#
# class UserManager(BaseUserManager):
#     def _create_user(self, username, password, email,
#                      is_superuser):
#         """
#         Creates and saves a User with the given email and password.
#         """
#         now = timezone.now()
#         if not username:
#             raise ValueError('The given username must be set')
#         if is_superuser:
#             roles = 'ROLE_SUPERADMIN'
#         else:
#             roles = 'ROLE_MEMBER'
#
#         user = self.model(username=username,
#                           username_canonical=username.strip().lower(),
#                           email=email,
#                           email_canonical=self.normalize_email(email),
#                           password=password,
#                           is_active=True,
#                           roles=roles,
#                           last_login=now,
#                           created=now,
#                           updated=now,
#                           enabled=True,
#                           expired=False,
#                           locked=False,
#                           credentials_expired=False,
#                           is_superuser=is_superuser)
#         user.save(using=self._db)
#         return user
#
#     def create_user(self, username, email, password=None):
#         return self._create_user(username, password, email, False)
#
#     def create_superuser(self, username, password, email):
#         return self._create_user(username, password, email, True)
#
#
# class User(PermissionsMixin):
#     username = models.CharField(max_length=255)
#     username_canonical = models.CharField(unique=True, max_length=255)
#     email = models.CharField(max_length=255)
#     email_canonical = models.CharField(unique=True, max_length=255)
#     enabled = models.BooleanField()
#     salt = models.CharField(max_length=255)
#     password = models.CharField(max_length=255)
#     last_login = models.DateTimeField(blank=True, null=True)
#     locked = models.BooleanField()
#     expired = models.BooleanField()
#     expires_at = models.DateTimeField(blank=True, null=True)
#     confirmation_token = models.CharField(max_length=255, blank=True, null=True)
#     password_requested_at = models.DateTimeField(blank=True, null=True)
#     # Data in this field can only be de-seralized by php
#     roles = models.TextField()
#     credentials_expired = models.BooleanField()
#     credentials_expire_at = models.DateTimeField(blank=True, null=True)
#     mid = models.CharField(max_length=36, blank=True, null=True)
#     googleid = models.CharField(db_column='googleId', unique=True, max_length=255, blank=True,
#                                 null=True)  # Field name made lowercase.
#     googleaccesstoken = models.CharField(db_column='googleAccessToken', max_length=255, blank=True,
#                                          null=True)  # Field name made lowercase.
#     facebookid = models.CharField(db_column='facebookId', unique=True, max_length=255, blank=True,
#                                   null=True)  # Field name made lowercase.
#     facebookaccesstoken = models.CharField(db_column='facebookAccessToken', max_length=255, blank=True,
#                                            null=True)  # Field name made lowercase.
#     is_admin = models.BooleanField(default=False)
#     is_active = models.BooleanField()
#
#     created = models.DateTimeField()
#     updated = models.DateTimeField()
#
#     objects = UserManager()
#
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['email']
#
#     class Meta:
#
#         db_table = 'users'
#
#     def __unicode__(self):
#         return u'%s %s %s' % (self.id, self.username, self.email)
#
#     def is_authenticated(self):
#         return True
#
#     def is_anonymous(self):
#         return False
#
#     def has_module_perms(self, app_label):
#         "Does the user have permissions to view the app `app_label`?"
#         # Simplest possible answer: Yes, always
#         return True
#
#     def is_staff(self):
#         return self.is_admin
#
#     def check_password(self, raw_password):
#         # TODO: Make this auto update using
#         # check_passwords setter argument
#         return check_password(raw_password, self.password)
#
#     def set_password(self, password):
#         from django.utils.crypto import get_random_string
#         if not self.salt:
#             self.salt = get_random_string()
#         self.password = make_password(password, salt=self.salt)
#
#     def get_role(self):
#         return self.roles
#
#     def assign_role(self):
#
#         from disa.roles import Admin, Member, Staff, SuperAdmin
#         user = User.objects.get(pk=self.id)
#         if self.roles == 'ROLE_ADMIN':
#             Admin.assign_role_to_user(user)
#         elif self.roles == 'ROLE_MEMBER':
#             Member.assign_role_to_user(user)
#         elif self.roles == 'ROLE_STAFF':
#             Staff.assign_role_to_user(user)
#         elif self.roles == 'ROLE_SUPERADMIN':
#             SuperAdmin.assign_role_to_user(user)
#         else:
#             Member.assign_role_to_user(user)
#
#     def save(self, *args, **kwargs):
#         assign = False
#         # Editing existing user
#         try:
#             orig = User.objects.get(pk=self.pk)
#             if orig.roles != self.roles:
#                 assign = True
#
#             if orig.enabled != self.enabled:
#                 self.is_active = self.enabled
#         # Creating new user
#         except:
#             self.set_password(self.password)
#             assign = True
#
#         if self.roles == 'ROLE_ADMIN' or self.roles == 'ROLE_SUPERADMIN':
#             self.is_superuser = True
#             self.is_admin = True
#
#         super(User, self).save()
#         if assign:
#             self.assign_role()
#
#
# class BaseModel(models.Model):
#     created_at = models.DateTimeField(default=timezone.now, editable=False, db_column='created')
#     updated_at = models.DateTimeField(default=timezone.now, editable=False, db_column='updated')
#
#     # created_by = models.ForeignKey(User, db_column='createdBy', editable=False, blank=True, null=True,
#     #                                related_name="%(class)s_created_by")
#     # updated_by = models.ForeignKey(User, db_column='updatedBy', editable=False, blank=True, null=True,
#     #                                related_name="%(class)s_updated_by")
#
#
#     class Meta:
#         abstract = True
#
#     def save(self, *args, **kwargs):
#         current_user = get_current_user()
#         if current_user and not current_user.is_anonymous() and isinstance(current_user, User):
#             if not getattr(self, 'id', None):
#                 self.created_by_id = current_user.id
#             self.updated_by_id = current_user.id
#
#         if not self.id:
#             self.created = timezone.now()
#         self.updated = timezone.now()
#
#         super(BaseModel, self).save()
#
#
# class SVExtra(models.Model):
#     title = models.CharField(max_length=255)
#     body = models.TextField()
#
#     class Meta:
#         db_table = 'SVExtra'
#
#     def __unicode__(self):
#         return u'%s%s' % (self.title, self.body)
#
#
# class NakshatramType(models.Model):
#     nakshatram = models.CharField(primary_key=True, max_length=63)
#
#     class Meta:
#         db_table = 'nakshatramTypes'
#
#     def __unicode__(self):
#         return u'%s' % self.nakshatram
#
#
# class PadamType(models.Model):
#     padam = models.CharField(primary_key=True, max_length=1)
#
#     class Meta:
#         db_table = 'padamTypes'
#
#     def __unicode__(self):
#         return u'%s' % self.padam
#
#
# class PakshamType(models.Model):
#     paksham = models.CharField(primary_key=True, max_length=11)
#
#     class Meta:
#         db_table = 'pakshamTypes'
#
#     def __unicode__(self):
#         return u'%s' % (self.paksham)
#
#
# class MaasamType(models.Model):
#     maasam = models.CharField(primary_key=True, max_length=21)
#
#     class Meta:
#         db_table = 'maasamTypes'
#
#     def __unicode__(self):
#         return u'%s' % self.maasam
#
#
# class TithiType(models.Model):
#     tithi = models.CharField(primary_key=True, max_length=15)
#
#     class Meta:
#         db_table = 'tithiTypes'
#
#     def __unicode__(self):
#         return u'%s' % self.tithi
#
#
# class RasiType(models.Model):
#     rasi = models.CharField(primary_key=True, max_length=63)
#
#     class Meta:
#         db_table = 'rasiTypes'
#
#     def __unicode__(self):
#         return u'%s' % (self.rasi)
#
#
# class SequenceNumber(models.Model):
#     id = models.CharField(primary_key=True, max_length=10)
#     number = models.IntegerField()
#
#     class Meta:
#         db_table = 'sequenceNumbers'
#
#     def __unicode__(self):
#         return u'%s%s' % (self.id, self.number)
#
#
# class Organisation(BaseModel):
#     id = models.CharField(primary_key=True, max_length=36)
#     code = models.CharField(max_length=20)
#     name = models.CharField(max_length=127)
#     description = models.CharField(max_length=255, blank=True, null=True)
#     city = models.CharField(max_length=63, blank=True, null=True)
#     address = models.CharField(max_length=511, blank=True, null=True)
#     state = models.CharField(max_length=127, blank=True, null=True)
#     country = models.CharField(max_length=63, blank=True, null=True)
#     pincode = models.CharField(max_length=15, blank=True, null=True)
#     email = models.CharField(max_length=255, blank=True, null=True)
#     phone = models.CharField(max_length=15, blank=True, null=True)
#     mobile = models.CharField(max_length=15, blank=True, null=True)
#     fax = models.CharField(max_length=15, blank=True, null=True)
#     website = models.CharField(max_length=255, blank=True, null=True)
#     parentid = models.CharField(db_column='parentId', max_length=36, blank=True,
#                                 null=True)  # Field name made lowercase.
#     owner = models.CharField(max_length=255)
#     status = models.BooleanField()
#     # created_by = models.CharField(db_column='createdBy', max_length=255, blank=True,
#     #                               null=True, editable=False)  # Field name made lowercase.
#     # updated_by = models.CharField(db_column='updatedBy', max_length=255, blank=True,
#     #                               null=True, editable=False)  # Field name made lowercase.
#     uri = models.CharField(max_length=127, blank=True, null=True)
#
#     # created = models.DateTimeField()
#     # updated = models.DateTimeField()
#
#     def __init__(self, *args, **kwargs):
#         super(Organisation, self).__init__(*args, **kwargs)
#         if not self.id:
#             self.id = str(uuid.uuid4())
#             # current_user = get_current_user()
#             # self.created_by = current_user.username
#             # self.updated_by = current_user.username
#             # self.created = timezone.now()
#             # self.updated = timezone.now()
#
#     class Meta:
#         db_table = 'organisations'
#
#     def __unicode__(self):
#         return '{0}, {1}'.format(self.name, self.city)
#
#         # def save(self, *args, **kwargs):
#         #     current_user = get_current_user()
#         #     if current_user and not current_user.is_anonymous() and isinstance(current_user, User):
#         #         if not self.pk:
#         #             self.created_by = current_user.username
#         #         self.updated_by = current_user.username
#         #
#         #     if not self.pk:
#         #         self.created = timezone.now()
#         #     self.updated = timezone.now()
#         #
#         #     super(Organisation, self).save()
#
#
# class SevaCategory(BaseModel):
#     id = models.CharField(primary_key=True, max_length=36, editable=False)
#     oid = models.ForeignKey(Organisation, db_column='oid')
#     code = models.CharField(unique=True, max_length=20)
#     amount = models.IntegerField()
#     location = models.CharField(max_length=63, blank=True, null=True)
#     last_sequence_number = models.CharField(db_column='lastSequenceNumber', max_length=11)  # Field name made lowercase.
#     name = models.CharField(max_length=255)
#     # created = models.DateTimeField()
#     # updated = models.DateTimeField()
#     # created_by = models.CharField(db_column='createdBy', max_length=255, blank=True,
#     #                               null=True)  # Field name made lowercase.
#     # updated_by = models.CharField(db_column='updatedBy', max_length=255, blank=True,
#     #                               null=True)  # Field name made lowercase.
#     status = models.BooleanField()
#     recurrence = models.CharField(max_length=25, blank=True, null=True)
#     show_start_date = models.BooleanField(db_column='showStartDate', default=True, null=False)
#     show_default_calendar_only = models.BooleanField(db_column='showDefaultCalendarOnly', default=False, null=False)
#     is_puja_held = models.BooleanField(db_column='isPujaHeld', default=True, null=False)
#     # sponsor_item_type = models.CharField(db_column='sponsorItemType',max_length=55, null=True, blank=True)
#     sponsor_item_category = models.ForeignKey('SponsorItemCategory', null=True)
#     language = models.CharField(db_column='language', max_length=55, null=True, blank=True)
#     # Deprecated. Do not use it any more. Only kept for backward compatibility. User Duration model instead.
#     duration = models.CharField(max_length=11, blank=True, null=True)
#     duration_type = models.CharField(db_column='durationType', max_length=11, blank=True, null=True)
#
#     def __init__(self, *args, **kwargs):
#         super(SevaCategory, self).__init__(*args, **kwargs)
#         if not self.id:
#             self.id = str(uuid.uuid4())
#
#             # current_user = get_current_user()
#             # self.created_by = current_user.username
#             # self.updated_by = current_user.username
#             # self.created = timezone.now()
#             # self.updated = timezone.now()
#
#     class Meta:
#         db_table = 'sevaCategories'
#
#     def __unicode__(self):
#         return "{0} - {1}".format(self.name, self.oid)
#
#
# BOOLEAN_YES = 1
# BOOLEAN_NO = 0
# status_choices = (
#     (BOOLEAN_NO, "Inactive"),
#     (BOOLEAN_YES, "Active")
# )
#
# DURATION_DAY = 'day'
# DURATION_MONTH = 'month'
# DURATION_YEAR = 'year'
# DURATION_LIFE = 'life_time'
# DURATION_CUSTOME = 'custom'
# duration_type_choices = (
#     (DURATION_DAY, 'Days'),
#     (DURATION_MONTH, 'Months'),
#     (DURATION_YEAR, 'Years'),
#     (DURATION_LIFE, 'Life time'),
#     (DURATION_CUSTOME, 'Custom')
# )
#
#
# class Duration(BaseModel):
#     seva_category = models.ForeignKey(SevaCategory, related_name='duration_seva_category')
#     duration = models.CharField(max_length=11, default='0')
#     duration_type = models.CharField(db_column='durationType', max_length=11, default=DURATION_LIFE,
#                                      choices=duration_type_choices)
#     amount = models.IntegerField(blank=True, null=True)
#     status = models.SmallIntegerField(choices=status_choices, default=BOOLEAN_YES)
#
#
# class Member(models.Model):
#     # id = models.CharField(primary_key=True, max_length=36, editable=False)
#     id = models.CharField(primary_key=True, max_length=36)
#
#     #    nakshatram = models.ForeignKey(NakshatramType, db_column='nakshatram', blank=True, null=True)
#     mid = models.IntegerField(unique=True)
#     salutation = models.CharField(max_length=63, blank=True, null=True)
#     name = models.CharField(max_length=63)
#     surname = models.CharField(max_length=63, blank=True, null=True)
#     display_name = models.CharField(db_column='displayName', max_length=15, blank=True,
#                                     null=True)  # Field name made lowercase.
#     place = models.CharField(max_length=63, blank=True, null=True)
#     gender = models.CharField(max_length=1, choices=gender_options, default='D')
#
#     calendar_type = models.CharField(max_length=15, choices=calendar_options, default='default')
#
#     maasam = models.ForeignKey(MaasamType, db_column='maasam', blank=True, null=True)
#
#     paksham = models.ForeignKey(PakshamType, db_column='paksham', blank=True, null=True)
#
#     tithi = models.ForeignKey(TithiType, db_column='tithi', blank=True, null=True)
#
#     rasi = models.ForeignKey(RasiType, db_column='rasi', blank=True, null=True)
#     nakshatram = models.ForeignKey(NakshatramType, db_column='nakshatram', blank=True, null=True)
#
#     birth_date = models.CharField(db_column='birthDate', max_length=4, blank=True,
#                                   null=True)  # Field name made lowercase.
#     birth_year = models.CharField(db_column='birthYear', max_length=4, blank=True,
#                                   null=True)  # Field name made lowercase.
#     email = models.CharField(max_length=128, blank=True, null=True)
#     phone = models.CharField(max_length=20, blank=True, null=True)
#     mobile = models.CharField(max_length=24, blank=True, null=True)
#     photo = models.CharField(max_length=127, blank=True, null=True)
#     search = models.CharField(max_length=256, blank=True, null=True)
#     gotram = models.CharField(max_length=127, blank=True, null=True)
#     created = models.DateTimeField()
#     updated = models.DateTimeField()
#     created_by = models.CharField(db_column='createdBy', max_length=255, blank=True,
#                                   null=True)  # Field name made lowercase.
#     updated_by = models.CharField(db_column='updatedBy', max_length=255, blank=True,
#                                   null=True)  # Field name made lowercase.
#     dob = models.DateField(blank=True, null=True)
#     googleid = models.CharField(db_column='googleId', max_length=255, blank=True,
#                                 null=True)  # Field name made lowercase.
#     facebookid = models.CharField(db_column='facebookId', max_length=255, blank=True,
#                                   null=True)  # Field name made lowercase.
#     twitterid = models.CharField(db_column='twitterId', max_length=255, blank=True,
#                                  null=True)  # Field name made lowercase.
#
#     class Meta:
#
#         db_table = 'members'
#
#     def __unicode__(self):
#         return "MID#{0} - {1}, {2}".format(self.mid, self.name.strip(), self.place.strip() if self.place else "")
#
#     def my_property(self):
#         if Address.objects.filter(mid=self.id):
#             return Address.objects.filter(mid=self.id)[0]
#         return
#
#     full_address = property(my_property)
#
#     def __init__(self, *args, **kwargs):
#         super(Member, self).__init__(*args, **kwargs)
#         if not self.id:
#             self.id = str(uuid.uuid4())
#
#     '''
#     Overriding the save() method on updating existing member details, creating new member for sending Emails onsubmit Save button
#     '''
#
#     def save(self, *args, **kwargs):
#         notify = False
#         self.name = ' '.join(word[0].upper() + word[1:] for word in self.name.split())
#         # Modifying existing member
#         try:
#
#             orig = Member.objects.get(pk=self.pk)
#
#             # Updating birth_date and birth_year
#             if orig.dob != self.dob:
#                 self.birth_date = self.dob.strftime("%m%d")
#                 self.birth_year = self.dob.strftime("%Y")
#
#             # Check if there is any change
#             if orig.mobile != self.mobile:
#                 template = get_template('mobileChange.html')
#                 message_html = template.render({
#                     'member_slt': self.salutation,
#                     'member_name': self.name
#                 })
#
#                 subject = 'Mobile Number Change'
#                 message_sms = str(render_to_string('mobileChange.txt')).format(name=self.salutation + ' ' + self.name)
#                 notify = True
#
#         # New member registration
#         except:
#
#             template = get_template('MemberRegistration.html')
#             message_html = template.render(
#                 {
#                     'member_slt': self.salutation,
#                     'member_name': self.name,
#                     'member_mid': self.mid
#                 })
#
#             subject = 'Member Registration'
#             message_sms = str(render_to_string('MemberRegistration.txt')).format(name=self.salutation + ' ' + self.name,
#                                                                                  mid=self.mid)
#             notify = True
#
#         if self.mobile is not None and notify != False:
#             number = self.mobile
#             send_SMS(number, message_sms)
#
#         if self.email is not None and notify != False:
#             to = [self.email]
#             sendmail(to, subject, None, message_html)
#
#         super(Member, self).save(*args, **kwargs)
#
#
# class Seva(models.Model):
#     id = models.CharField(primary_key=True, max_length=36, editable=False)
#     sid = models.ForeignKey(SevaCategory, db_column='sid')
#     oid = models.ForeignKey(Organisation, db_column='oid')
#     mid = models.ForeignKey(Member, db_column='mid', related_name='sevas')
#     #    nakshatram = models.ForeignKey(NakshatramType, db_column='nakshatram', blank=True, null=True)
#     #     smid = models.CharField(max_length=36, blank=True, null=True)
#     ssid = models.CharField(unique=True, max_length=36)
#
#     calendar_type = models.CharField(max_length=15, choices=calendar_options, default='default')
#
#     maasam = models.ForeignKey(MaasamType, db_column='maasam', blank=True, null=True)
#
#     paksham = models.ForeignKey(PakshamType, db_column='paksham', blank=True, null=True)
#
#     tithi = models.ForeignKey(TithiType, db_column='tithi', blank=True, null=True)
#
#     raasi = models.ForeignKey(RasiType, db_column='raasi', blank=True, null=True)
#     nakshatram = models.ForeignKey(NakshatramType, db_column='nakshatram', blank=True, null=True)
#
#     sevadate = models.CharField(db_column='sevaDate', max_length=63, blank=True,
#                                 null=True)  # Field name made lowercase.
#     sevaday = models.CharField(db_column='sevaDay', max_length=4, blank=True, null=True)  # Field name made lowercase.
#     islunar = models.CharField(db_column='isLunar', max_length=4, blank=True, null=True)  # Field name made lowercase.
#     inthenameof = models.CharField(db_column='inTheNameOf', max_length=127, blank=True,
#                                    null=True)  # Field name made lowercase.
#     gotram = models.CharField(max_length=127, blank=True, null=True)
#     occasion = models.CharField(max_length=40, blank=True, null=True)
#     startdate = models.DateField(db_column='startDate', blank=True, null=True)  # Field name made lowercase.
#     enddate = models.DateField(db_column='endDate', blank=True, null=True)  # Field name made lowercase.
#     created = models.DateTimeField()
#     updated = models.DateTimeField()
#     created_by = models.CharField(db_column='createdBy', max_length=255, blank=True,
#                                   null=True)  # Field name made lowercase.
#     updated_by = models.CharField(db_column='updatedBy', max_length=255, blank=True,
#                                   null=True)  # Field name made lowercase.
#     sevadatestd = models.DateField(db_column='sevaDateStd', blank=True, null=True)  # Field name made lowercase.
#     title = models.CharField(max_length=55, blank=True, null=True)
#
#     class Meta:
#         db_table = 'sevas'
#
#     def __unicode__(self):
#         return u'%s. %s - %s.' % (self.mid, self.ssid, self.sid)
#
#     def __init__(self, *args, **kwargs):
#         super(Seva, self).__init__(*args, **kwargs)
#         if not self.id:
#             self.id = str(uuid.uuid4())
#
#     '''
#     Overriding the save() method on updating existing seva details,creating new sevas for sending Emails
#     '''
#
#     def save(self, *args, **kwargs):
#         notify = False
#
#         cur = connection.cursor()
#
#         S_mid = "" + str(self.mid) + ""
#
#         query = "Select name,email,salutation,mobile From members Where " + " '" + S_mid.split('(')[
#             0] + " '" + "= members.mid"
#         cur.execute(query)
#         result = cur.fetchone()
#         name = result[0]
#         # name = ' '.join(word[0].upper()+word[1:] for word in name.split())
#         email = result[1]
#         salutation = result[2]
#         number = result[3]
#
#         # Modifying existing seva
#         try:
#
#             orig = Seva.objects.get(pk=self.pk)
#
#             # Check if there is any change
#             if orig.sevaday != self.sevaday:
#                 template = 'SevadayChange.html'
#                 subject = 'Seva Day Change'
#                 message_sms = str(render_to_string('SevadayChange.txt')).format(name=salutation + ' ' + name,
#                                                                                 ssid=self.ssid)
#                 notify = True
#
#             elif orig.occasion != self.occasion:
#                 template = 'OccasionChange.html'
#                 subject = 'Seva occasion Change'
#                 message_sms = str(render_to_string('OccasionChange.txt')).format(name=salutation + ' ' + name,
#                                                                                  ssid=self.ssid)
#                 notify = True
#
#
#         # New seva registration
#         except:
#
#             template = 'SevaRegistration.html'
#             subject = 'Seva Registration'
#             message_sms = str(render_to_string('SevaRegistration.txt')).format(name=salutation + ' ' + name,
#                                                                                ssid=self.ssid)
#             notify = True
#
#         if number is not None and notify != False:
#             send_SMS(number, message_sms)
#
#         if email is not None and notify != False:
#             template = get_template(template)
#             message_html = template.render(
#                 {
#                     'seva_ssid': self.ssid,
#                     'member_slt': salutation,
#                     'member_name': name,
#                     'seva_id': self.ssid
#                 })
#             to = [email]
#             sendmail(to, subject, None, message_html)
#
#         super(Seva, self).save(*args, **kwargs)
#
#     def __init__(self, *args, **kwargs):
#         super(Seva, self).__init__(*args, **kwargs)
#         if not self.id:
#             self.id = str(uuid.uuid4())
#
#
# class Address(models.Model):
#     # id = models.CharField(primary_key=True, max_length=36, editable=False)
#     id = models.CharField(primary_key=True, max_length=36)
#     mid = models.ForeignKey(Member, db_column='mid', related_name='addresses')
#     is_primary = models.BooleanField(db_column='isPrimary')  # Field name made lowercase.
#     address = models.CharField(max_length=512)
#     city = models.CharField(max_length=48, blank=True, null=True, db_index=True)
#     district = models.CharField(max_length=48, blank=True, null=True)
#     state = models.CharField(max_length=20, blank=True, null=True)
#     country = models.CharField(max_length=20, blank=True, null=True)
#     pin = models.CharField(max_length=16, blank=True, null=True)
#     phone = models.CharField(max_length=20, blank=True, null=True)
#     is_valid = models.BooleanField(db_column='isValid', default=True)  # Field name made lowercase.
#     created = models.DateTimeField()
#     updated = models.DateTimeField()
#     created_by = models.CharField(db_column='createdBy', max_length=255, blank=True,
#                                   null=True)  # Field name made lowercase.
#     updated_by = models.CharField(db_column='updatedBy', max_length=255, blank=True,
#                                   null=True)  # Field name made lowercase.
#
#     def __init__(self, *args, **kwargs):
#         super(Address, self).__init__(*args, **kwargs)
#         if not self.id:
#             self.id = str(uuid.uuid4())
#
#     class Meta:
#
#         db_table = 'addresses'
#
#     def __unicode__(self):
#         return u'%s%s%s%s%s%s%s' % (
#             self.id, self.address, self.city, self.district, self.state, self.country, self.phone)
#
#     def my_property(self):
#         return format_html('<ul class="nav nav-pills nav-stacked">%s<br>%s<br>%s<br>%s<br>%s<br>%s</ul>' % (
#             self.address, self.city, self.district, self.state, self.country, self.pin))
#
#     my_property.short_description = "Full Address"
#     full_address = property(my_property)
#
#     def color_tags(self):
#         if not self.is_valid:
#             return format_html('<span class="label label-danger">Invalid</span>')
#
#         if self.is_primary:
#             return format_html('<span class="label label-primary">Primary</span>')
#
#     '''
#     Here overriding the save() method on updating existing address for sending Email on submitting Save button.
#     '''
#
#     def save(self):
#         notify = False
#
#         cur = connection.cursor()
#
#         Ad_mid = "" + str(self.mid) + ""
#
#         query = "Select name,email,salutation,mobile From members Where " + " '" + Ad_mid.split('(')[
#             0] + " '" + "= members.mid"
#         print query
#         cur.execute(query)
#         result = cur.fetchone()
#         name = result[0]
#         email = result[1]
#         salutation = result[2]
#         number = result[3]
#
#         query2 = " Select id From members where mid=" + " '" + Ad_mid.split('(')[0] + " '"
#         cur.execute(query2)
#         reslt = cur.fetchone()
#
#         '''comparing in between sevaDate and currentDate which should not be more than 30 days for sending Email'''
#
#         query3 = "Select sevadate From sevas Where mid=" + " '" + reslt[
#             0] + " '" + "AND sevaDate BETWEEN CURDATE() - INTERVAL 30 DAY AND CURDATE();"
#         cur.execute(query3)
#         rslt = cur.fetchone()
#         seva_date = None
#         if rslt is not None:
#             seva_date = rslt[0]
#
#         # Modifying existing seva
#         try:
#
#             orig = Address.objects.get(pk=self.pk)
#
#             # Check if there is any change
#             if orig.address != self.address or orig.city != self.city or orig.district != self.district or orig.state != self.state or orig.country != self.country:
#                 template = 'addressChange.html'
#                 subject = 'Address Change'
#                 message_sms = str(render_to_string('addressChange.txt')).format(name=salutation + ' ' + name)
#                 notify = True
#
#             elif seva_date is not None and orig.is_valid != self.is_valid and not self.is_valid:
#                 template = 'wrongAddress.html'
#                 subject = 'Wrong Address'
#                 message_sms = str(render_to_string('wrongAddress.txt')).format(name=salutation + ' ' + name,
#                                                                                date=seva_date)
#                 notify = True
#         except:
#             pass
#
#         if number is not None and notify != False:
#             send_SMS(number, message_sms)
#
#         if email is not None and notify != False:
#             message_html = get_template(template).render(
#                 Context({
#                     'member_slt': salutation,
#                     'member_name': name,
#                     'seva_date': seva_date
#
#                 })
#             )
#             to = [email]
#             sendmail(to, subject, None, message_html)
#
#         super(Address, self).save()
#
#
# class AddressAdmin(admin.ModelAdmin):
#     def get_name(self, obj):
#         return obj.mid.name
#
#     # get_name.admin_order_field  = 'mid'  #Allows column order sorting
#     get_name.short_description = 'Member name'  # Renames column head
#     list_display = ('full_address', 'color_tags', 'mid',)
#     '''problem with mid field...its concatenating member name also'''
#     list_filter = ('state', 'country',)
#     search_fields = ('address', 'city', 'district',)
#
#
# class Awardee(models.Model):
#     mid = models.CharField(max_length=36)
#     name = models.CharField(max_length=50)
#     year = models.CharField(max_length=4)
#     description = models.CharField(max_length=512, blank=True, null=True)
#     specialization = models.CharField(max_length=52, blank=True, null=True)
#     member = models.ForeignKey(Member, db_column='member')
#
#     class Meta:
#         db_table = 'awardees'
#
#     def __unicode__(self):
#         return '%s%s%s%s%s%s' % (self.mid, self.name, self.year, self.description, self.specialization, self.member)
#
#
# class AwardeeAdmin(admin.ModelAdmin):
#     list_display = ('mid', 'name', 'year', 'description', 'specialization', 'member',)
#     list_filter = ('year', 'specialization',)
#     search_fields = ('member',)
#
#
# class LunarDate(models.Model):
#     maasam = models.ForeignKey(MaasamType, db_column='maasam')
#     paksham = models.ForeignKey(PakshamType, db_column='paksham', blank=True, null=True)
#     tithi = models.ForeignKey(TithiType, db_column='tithi')
#     day = models.IntegerField()
#     month = models.IntegerField()
#     year = models.IntegerField()
#
#     class Meta:
#         db_table = 'lunarDates'
#
#     def __unicode__(self):
#         return u'%s%s%s%s%s%s' % (self.maasam, self.paksham, self.tithi, self.day, self.month, self.year)
#
#
# class LunarAdmin(admin.ModelAdmin):
#     list_display = ('maasam', 'paksham', 'tithi', 'day', 'month', 'year',)
#     # list_filter = ('year')
#     # search_fields = ('maasam','paksham')
#
#
# class MembersAdmin(ExportMixin, admin.ModelAdmin):
#     list_display = ('mid', 'nakshatram', 'name', 'salutation',)
#     # list_filter = ('mid')
#     # search_fields = ('mid')
#     model = Member
#     form = modelform_factory(Member, form=MemberForm, fields='__all__')
#     fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('id',
#                        'mid',
#                        'salutation',
#                        'name',
#                        'surname',
#                        'place',
#                        'gender',
#                        'calendar_type',
#                        'maasam',
#                        'paksham',
#                        'tithi',
#                        'rasi',
#                        'nakshatram',
#                        'dob',
#                        'email',
#                        'phone',
#                        'mobile',
#                        'gotram',
#                        'created',
#                        'updated',
#                        'googleid',
#                        'facebookid',
#                        'twitterid',
#                        'created_by',
#                        'updated_by',
#                        )
#         }),
#     )
#
#
# class NakshatramRasiPadamData(models.Model):
#     nakshatram = models.ForeignKey(NakshatramType, db_column='nakshatram')
#     padam = models.ForeignKey(PadamType, db_column='padam')
#     rasi = models.ForeignKey(RasiType, db_column='rasi')
#     created = models.DateTimeField()
#     updated = models.DateTimeField()
#     created_by = models.CharField(db_column='createdBy', max_length=255, blank=True,
#                                   null=True)  # Field name made lowercase.
#     updated_by = models.CharField(db_column='updatedBy', max_length=255, blank=True,
#                                   null=True)  # Field name made lowercase.
#
#     class Meta:
#
#         db_table = 'nakshatramRasiPadamData'
#
#     def __unicode__(self):
#         return u'%s%s%s%s%s%s%s' % (
#             self.nakshatram, self.padam, self.rasi, self.created, self.updated, self.created_by, self.updated_by)
#
#     def save(self, *args, **kwargs):
#         current_user = get_current_user()
#         if current_user and not current_user.is_anonymous() and isinstance(current_user, User):
#             if not getattr(self, 'id', None):
#                 self.created_by = current_user.username
#             self.updated_by = current_user.username
#
#         if not self.id:
#             self.created = timezone.now()
#         self.updated = timezone.now()
#
#         super(NakshatramRasiPadamData, self).save()
#
#
# class NakshatramRasiPadamDataAdmin(admin.ModelAdmin):
#     list_display = ('nakshatram', 'padam', 'rasi', 'created', 'updated', 'created_by', 'updated_by',)
#
#
# class NakshatramTypeAdmin(admin.ModelAdmin):
#     list_display = ('nakshatram',)
#
#
# class OauthClient(models.Model):
#     random_id = models.CharField(max_length=255)
#     # This field can be de-serialised only in php
#     redirect_uris = models.TextField()
#     secret = models.CharField(max_length=255)
#     # This field can be de-serialised only in php
#     allowed_grant_types = models.TextField()
#     name = models.CharField(max_length=30, blank=True, null=True)
#
#     class Meta:
#         db_table = 'oauthClient'
#
#     def __unicode__(self):
#         return u'%s%s%s%s%s' % (self.random_id, self.secret, self.allowed_grant_types, self.name, self.redirect_uri)
#
#
# class OauthAccesstoken(models.Model):
#     user = models.ForeignKey(User, blank=True, null=True)
#     client = models.ForeignKey(OauthClient)
#     token = models.CharField(unique=True, max_length=255)
#     expires_at = models.IntegerField(blank=True, null=True)
#     scope = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         db_table = 'oauthAccessToken'
#
#     def __unicode__(self):
#         return u'%s%s%s%s%s' % (self.token, self.client, self.user, self.expires_at, self.scope)
#
#
# class OauthAccessTokenAdmin(admin.ModelAdmin):
#     list_display = ('user', 'token', 'client', 'expires_at', 'scope',)
#
#
# class OauthAuthCode(models.Model):
#     user = models.ForeignKey(User, blank=True, null=True)
#     client = models.ForeignKey(OauthClient)
#     token = models.CharField(unique=True, max_length=255)
#     redirect_uri = models.TextField()
#     expires_at = models.IntegerField(blank=True, null=True)
#     scope = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         db_table = 'oauthAuthCode'
#
#     def __unicode__(self):
#         return u'%s%s%s%s%s%s' % (self.token, self.client, self.user, self.expires_at, self.scope, self.redirect_uri)
#
#
# class OauthRefreshToken(models.Model):
#     user = models.ForeignKey(User, blank=True, null=True)
#     client = models.ForeignKey(OauthClient, blank=True, null=True)
#     token = models.CharField(unique=True, max_length=255)
#     expires_at = models.IntegerField(blank=True, null=True)
#     scope = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         db_table = 'oauthRefreshTokens'
#
#     def __unicode__(self):
#         return u'%s%s%s%s%s' % (self.user, self.client, self.token, self.expires_at, self.scope)
#
#
# class Profile(models.Model):
#     id = models.CharField(primary_key=True, max_length=36)
#     mid = models.ForeignKey(Member, db_column='mid', unique=True)
#     padam = models.ForeignKey(PadamType, db_column='padam', blank=True, null=True)
#     janmasamvatsara = models.CharField(db_column='janmaSamvatsara', max_length=127, blank=True,
#                                        null=True)  # Field name made lowercase.
#     timeofbirth = models.CharField(db_column='timeOfBirth', max_length=127, blank=True,
#                                    null=True)  # Field name made lowercase.
#     placeofbirth = models.CharField(db_column='placeOfBirth', max_length=127, blank=True,
#                                     null=True)  # Field name made lowercase.
#     countryofbirth = models.CharField(db_column='countryOfBirth', max_length=35, blank=True,
#                                       null=True)  # Field name made lowercase.
#     citizen = models.CharField(max_length=35, blank=True, null=True)
#     sutram = models.CharField(max_length=127, blank=True, null=True)
#     vaasara = models.CharField(max_length=45, blank=True, null=True)
#     religion = models.CharField(max_length=48, blank=True, null=True)
#     areasofinterest = models.CharField(db_column='areasOfInterest', max_length=127, blank=True,
#                                        null=True)  # Field name made lowercase.
#     associationsince = models.IntegerField(db_column='associationSince', blank=True,
#                                            null=True)  # Field name made lowercase.
#     community = models.CharField(max_length=20, blank=True, null=True)
#     subsect = models.CharField(db_column='subSect', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     mantropadesha = models.NullBooleanField(blank=True, null=True)
#     kriyayoga = models.NullBooleanField(db_column='kriyaYoga', blank=True, null=True)  # Field name made lowercase.
#     sdhsmember = models.NullBooleanField(db_column='SDHSMember', blank=True, null=True)  # Field name made lowercase.
#     localashramassociation = models.IntegerField(db_column='localAshramAssociation', blank=True,
#                                                  null=True)  # Field name made lowercase.
#     bloodgroup = models.CharField(db_column='bloodGroup', max_length=5, blank=True,
#                                   null=True)  # Field name made lowercase.
#     availablehrsperweek = models.IntegerField(db_column='availableHrsPerWeek', blank=True,
#                                               null=True)  # Field name made lowercase.
#     deathdate = models.CharField(db_column='deathDate', max_length=45, blank=True,
#                                  null=True)  # Field name made lowercase.
#     isprimary = models.NullBooleanField(db_column='isPrimary', blank=True, null=True)  # Field name made lowercase.
#     indianprofile = models.NullBooleanField(db_column='indianProfile', blank=True,
#                                             null=True)  # Field name made lowercase.
#     profilestatus = models.CharField(db_column='profileStatus', max_length=15, blank=True,
#                                      null=True)  # Field name made lowercase.
#     created = models.DateTimeField()
#     updated = models.DateTimeField()
#     created_by = models.CharField(db_column='createdBy', max_length=255, blank=True,
#                                   null=True)  # Field name made lowercase.
#     updated_by = models.CharField(db_column='updatedBy', max_length=255, blank=True,
#                                   null=True)  # Field name made lowercase.
#     janmatithi = models.ForeignKey(TithiType, db_column='janmaTithi', blank=True,
#                                    null=True)  # Field name made lowercase.
#     janmapaksha = models.ForeignKey(PakshamType, db_column='janmaPaksha', blank=True,
#                                     null=True)  # Field name made lowercase.
#     janmamaasa = models.ForeignKey(MaasamType, db_column='janmaMaasa', blank=True,
#                                    null=True)  # Field name made lowercase.
#
#     class Meta:
#
#         db_table = 'profiles'
#
#     def save(self, *args, **kwargs):
#         current_user = get_current_user()
#         if current_user and not current_user.is_anonymous() and isinstance(current_user, User):
#             if self.id:
#                 self.updated_by = current_user.username
#             else:
#                 self.created_by = current_user.username
#                 self.updated_by = current_user.username
#
#         if self.id:
#             self.updated = timezone.now()
#         else:
#             self.created = timezone.now()
#             self.updated = timezone.now()
#
#         super(Profile, self).save()
#
#     def __unicode__(self):
#         return u'%s%s%s%s%s%s%s' % (
#             self.id, self.mid, self.padam, self.janmasamvatsara, self.timeofbirth, self.countryofbirth, self.citizen)
#
#
# class SevaAddress(models.Model):
#     id = models.CharField(primary_key=True, max_length=36, editable=False)
#     sid = models.OneToOneField(Seva, db_column='sid', unique=True, related_name='seva_address')
#     address = models.CharField(max_length=512)
#     city = models.CharField(max_length=48, blank=True, null=True)
#     district = models.CharField(max_length=48, blank=True, null=True)
#     state = models.CharField(max_length=20, blank=True, null=True)
#     country = models.CharField(max_length=20, blank=True, null=True)
#     pin = models.CharField(max_length=16, blank=True, null=True)
#     phone = models.CharField(max_length=20, blank=True, null=True)
#     isvalid = models.BooleanField(db_column='isValid')  # Field name made lowercase.
#     created = models.DateTimeField()
#     updated = models.DateTimeField()
#     created_by = models.CharField(db_column='createdBy', max_length=255, blank=True,
#                                   null=True)  # Field name made lowercase.
#     updated_by = models.CharField(db_column='updatedBy', max_length=255, blank=True,
#                                   null=True)  # Field name made lowercase.
#
#     def __init__(self, *args, **kwargs):
#         super(SevaAddress, self).__init__(*args, **kwargs)
#         if not self.id:
#             self.id = str(uuid.uuid4())
#
#         current_user = get_current_user()
#         self.created_by = current_user.username
#         self.updated_by = current_user.username
#         self.created = timezone.now()
#         self.updated = timezone.now()
#
#     class Meta:
#
#         db_table = 'sevaAddresses'
#
#     def __unicode__(self):
#         return u'%s' % (self.sid)
#
#     def save(self, *args, **kwargs):
#         current_user = get_current_user()
#         if current_user and not current_user.is_anonymous() and isinstance(current_user, User):
#             if not self.id:
#                 self.created_by = current_user.username
#             self.updated_by = current_user.username
#
#         if not self.id:
#             self.created = timezone.now()
#         self.updated = timezone.now()
#
#         super(SevaAddress, self).save()
#
#
# class SevasAddress(models.Model):
#     seva = models.ForeignKey(Seva, on_delete=models.CASCADE)
#     address = models.ForeignKey(Address, on_delete=models.CASCADE)
#
#     class Meta:
#         db_table = 'seva_address'
#         unique_together = (('seva', 'address'),)
#
#
# class SevasAddressAdmin(admin.ModelAdmin):
#     list_display = ('seva', 'address',)
#
#
# class SevasAdmin(ExportMixin, admin.ModelAdmin):
#     list_display = ('mid', 'nakshatram', 'ssid', 'sevadate', 'sevaday',)
#     list_filter = ('sevadate', ('created', DateRangeFilter),)
#     # list_filter = ('sevadate', DateFieldListFilter)
#     search_fields = ('sevaday',)
#     # date_hierarchy = 'created'
#     model = Seva
#     form = modelform_factory(Seva, form=SevaForm, fields='__all__')
#     fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('id',
#                        'sid',
#                        'oid',
#                        'mid',
#                        'ssid',
#                        'calendar_type',
#                        'maasam',
#                        'paksham',
#                        'tithi',
#                        'raasi',
#                        'nakshatram',
#                        'sevadate',
#                        'sevaday',
#                        'islunar',
#                        'inthenameof',
#                        'gotram',
#                        'occasion',
#                        'startdate',
#                        'enddate',
#                        'created',
#                        'updated',
#                        'created_by',
#                        'updated_by',
#                        'sevadatestd',
#                        )
#         }),
#     )
#
#
# class Tag(models.Model):
#     member = models.CharField(max_length=36)
#     tag = models.CharField(max_length=255)
#
#     class Meta:
#         db_table = 'tags'
#
#
# class Transaction(models.Model):
#     transactiontype = models.CharField(db_column='transactionType', max_length=20)  # Field name made lowercase.
#     transactionamount = models.CharField(db_column='transactionAmount', max_length=45)  # Field name made lowercase.
#     checknumber = models.CharField(db_column='checkNumber', max_length=20)  # Field name made lowercase.
#     cardtype = models.CharField(db_column='cardType', max_length=20)  # Field name made lowercase.
#     cardnumber = models.CharField(db_column='cardNumber', max_length=45)  # Field name made lowercase.
#     paymentdate = models.CharField(db_column='paymentDate', max_length=20)  # Field name made lowercase.
#     paymentmethod = models.CharField(max_length=20)
#     creditcardtype = models.CharField(db_column='creditCardType', max_length=20)  # Field name made lowercase.
#     lastfourdigits = models.CharField(db_column='lastFourDigits', max_length=4)  # Field name made lowercase.
#     isdomestic = models.BooleanField(db_column='isDomestic')  # Field name made lowercase.
#     transcurrencytype = models.CharField(db_column='transCurrencyType', max_length=20)  # Field name made lowercase.
#     comments = models.CharField(max_length=255)
#     created = models.DateTimeField()
#     updated = models.DateTimeField()
#     created_by = models.CharField(db_column='createdBy', max_length=255, blank=True,
#                                   null=True)  # Field name made lowercase.
#     updated_by = models.CharField(db_column='updatedBy', max_length=255, blank=True,
#                                   null=True)  # Field name made lowercase.
#     mid = models.ForeignKey(Member, db_column='mid')
#     oid = models.ForeignKey(Organisation, db_column='oid')
#     sid = models.ForeignKey(Seva, db_column='sid')
#     scid = models.ForeignKey(SevaCategory, db_column='scId')  # Field name made lowercase.
#
#     class Meta:
#
#         db_table = 'transactions'
#
#     def __unicode__(self):
#         return u'%s%s%s%s%s%s%s' % (
#             self.transactiontype, self.transactionamount, self.checknumber, self.cardtype, self.cardnumber,
#             self.paymentdate, self.paymentmethod, self.creditcardtype, self.lastfourdigits, self.isdomestic,
#             self.transcurrencytype)
#
#     def save(self, *args, **kwargs):
#         current_user = get_current_user()
#         if current_user and not current_user.is_anonymous() and isinstance(current_user, User):
#             if not getattr(self, 'id', None):
#                 self.created_by = current_user.username
#             self.updated_by = current_user.username
#
#         if not self.id:
#             self.created = timezone.now()
#         self.updated = timezone.now()
#
#         super(Transaction, self).save()
#
#
# class commonAdminMixin(object):
#     def __init__(self, model, admin_site):
#         self.list_display = [field.name for field in model._meta.fields if
#                              field.name not in ("id", 'created', 'updated', 'created_by', 'updated_by')]
#         super(commonAdminMixin, self).__init__(model, admin_site)
#
#
# class commonAdmin(commonAdminMixin, admin.ModelAdmin):
#     pass
#
#
# class DonationKind(BaseModel):
#     member = models.ForeignKey(Member, null=False, blank=False)
#     ocassionName = models.CharField(max_length=45, blank=True, null=True)
#     ocassionDate = models.DateField(blank=True, null=True)
#     organisation = models.ForeignKey(Organisation, blank=True, null=True)
#     material = models.CharField(max_length=45, blank=True, null=True)
#     quantity = models.FloatField(blank=True, null=True)
#     units = models.CharField(max_length=5, blank=True, null=True)
#     value = models.IntegerField(blank=True, null=True)
#     certifiedBy = models.CharField(max_length=30, blank=True, null=True)
#     dateOfDonation = models.DateField(blank=True, null=True)
#     notes = models.TextField(blank=False, null=False)
#
#     def __unicode__(self):
#         return u"%s-%s-%s-%s-%s-%s" % (self.member, self.organisation, self.material, self.quantity,
#                                        self.units, self.value)
#
#
# class DonationKindAdmin(admin.ModelAdmin):
#     list_display = ('id', 'member', 'ocassionName', 'organisation', 'material', 'dateOfDonation')
#     list_filter = ('organisation', 'ocassionName')
#     search_fields = ('member', 'ocassionName', 'organisation', 'material', 'dateOfDonation')
#
#     # def donationsKind_id(self, obj):
#     #     text = 'Donations Kind ID'
#     #     return '<a href="%s/%s" target="_blank">%s</a>' %('/py-admin/donationskind/', str(obj.id))
#
#
# class DonationCash(BaseModel):
#     member = models.ForeignKey(Member, null=False, blank=False)
#     ocassionName = models.CharField(max_length=45, blank=True, null=True)
#     ocassionDate = models.DateField(blank=True, null=True)
#     organisation = models.ForeignKey(Organisation, blank=True, null=True)
#     receiptNo = models.CharField(max_length=15, blank=True, null=True)
#     amount = models.IntegerField(blank=True, null=True)
#     instruementDetails = models.CharField(max_length=45, blank=True, null=True)
#     dateOfDonation = models.DateField(blank=True, null=True)
#     notes = models.TextField(blank=False, null=False)
#
#     def __unicode__(self):
#         return u"%s-%s-%s-%s" % (self.member, self.ocassionName, self.amount,
#                                  self.instruementDetails)
#
#
# class DonationCashAdmin(admin.ModelAdmin):
#     list_display = ('id', 'member', 'ocassionName', 'organisation', 'receiptNo', 'dateOfDonation')
#     list_filter = ('organisation', 'ocassionName')
#     search_fields = ('member', 'ocassionName', 'organisation', 'receiptNo', 'dateOfDonation')
#
#
# class DonationAsset(BaseModel):
#     ASSET_TYPE = (('land', 'Land'),
#                   ('building', 'Building'),
#                   ('equipment', 'Equipment'))
#     member = models.ForeignKey(Member, null=False, blank=False)
#     ocassionName = models.CharField(max_length=45, blank=True, null=True)
#     ocassionDate = models.DateField(blank=True, null=True)
#     organisation = models.ForeignKey(Organisation, blank=True, null=True)
#     assetType = models.CharField(max_length=20, blank=True, null=True, default='equipment', choices=ASSET_TYPE)
#     dateOfDonation = models.DateField(blank=True, null=True)
#     value = models.IntegerField(blank=True, null=True)
#     subType = models.CharField(max_length=20, blank=True, null=True)
#     assetLocation = models.CharField(max_length=150, blank=True, null=True)
#     dateOfRegistration = models.DateField(blank=True, null=True)
#     extent = models.CharField(max_length=20, blank=True, null=True)
#     notes = models.TextField(blank=False, null=False)
#
#     def __unicode__(self):
#         return u"%s-%s-%s-%s" % (self.member, self.ocassionName, self.assetType,
#                                  self.value)
#
#
# class DonationAssetAdmin(admin.ModelAdmin):
#     list_display = ('id', 'member', 'ocassionName', 'organisation', 'assetType', 'dateOfRegistration')
#     list_filter = ('organisation', 'ocassionName')
#     search_fields = ('member', 'ocassionName', 'organisation', 'assetType', 'dateOfRegistration')
#
#
# class DonationService(BaseModel):
#     capacity = models.CharField(max_length=30)
#     fromDate = models.DateField(blank=True, null=True)
#     toDate = models.DateField(blank=True, null=True)
#     ocassionName = models.CharField(max_length=45, blank=True, null=True)
#     organisation = models.ForeignKey(Organisation, blank=True, null=True)
#
#
# class DonationServiceAdmin(admin.ModelAdmin):
#     list_display = ('id', 'capacity', 'ocassionName', 'organisation')
#     list_filter = ('organisation', 'ocassionName')
#     search_fields = ('capacity', 'ocassionName', 'organisation')
#
#
# class SponsorItemCategory(BaseModel):
#     name = models.CharField(max_length=25)
#     desc = models.CharField(max_length=100, blank=True, null=True)
#
#     def __unicode__(self):
#         return self.name
#
#
# class SponsorItem(BaseModel):
#     code = models.CharField(max_length=25)
#     name = models.CharField(max_length=255)
#     category = models.ForeignKey(SponsorItemCategory)
#     description = models.CharField(max_length=523)
#     amount = models.FloatField()
#     photo = models.CharField(max_length=255, blank=True, null=True)
#     seva_id = models.ForeignKey(Seva, db_column='sevaId', unique=True)  # Field name made lowercase.
#
#     class Meta:
#         db_table = 'sponsorItems'
#
#     def __unicode__(self):
#         return "{0}, {1} ({2}) ".format(self.category, self.name, self.code)
#
#
# class GroupName(models.Model):
#     id = models.CharField(primary_key=True, max_length=21)
#     name = models.CharField(max_length=36, unique=True)
#
#     class Meta:
#         db_table = 'groupNames'
#
#     def __unicode__(self):
#         return u'%s' % self.name
#
#
# class GroupData(BaseModel):
#     gid = models.ForeignKey(GroupName, db_column='gid')
#     name = models.CharField(max_length=36)
#     surname = models.CharField(max_length=63, blank=True, null=True)
#     email = models.CharField(max_length=255, blank=True, null=True)
#     mobile = models.CharField(max_length=24, blank=True, null=True)
#
#     class Meta:
#         db_table = 'groupData'
#
#
# from django.contrib.gis.db import models
#
#
# class AssetLand(BaseModel):
#     areacode = models.CharField(max_length=63, blank=True, null=True)
#     doc = models.IntegerField(blank=True, null=True)
#     place = models.CharField(max_length=63, blank=True, null=True)
#     donee_vendee = models.CharField(max_length=63, blank=True, null=True)
#     regn_no = models.CharField(max_length=63, blank=True, null=True)
#     sub_registrar = models.CharField(max_length=63, blank=True, null=True)
#     land_type = models.CharField(max_length=15, choices=Land_Type)
#     salutation = models.CharField(max_length=15, choices=slt_type)
#     donor_vendor = models.CharField(max_length=65, blank=True, null=True)
#     relationship = models.CharField(max_length=15, choices=relation_type)
#     relative = models.CharField(max_length=63, blank=True, null=True)
#     acrage = models.CharField(max_length=63, blank=True, null=True)
#     yards = models.IntegerField(blank=True, null=True)
#     sqmeter = models.IntegerField(blank=True, null=True)
#     survey = models.CharField(max_length=83, blank=True, null=True)
#     address = models.TextField(max_length=250, blank=True, null=True)
#     state = models.CharField(max_length=63, choices=states)
#     value = models.IntegerField(help_text="(Value in Rs)", blank=True, null=True)
#     stamp_worth = models.IntegerField(blank=True, null=True)
#     regn_fees = models.IntegerField(blank=True, null=True, help_text="(in Rs)")
#     total = models.IntegerField(help_text="(Total in Rs)", blank=True, null=True)
#     east = models.CharField(max_length=63, blank=True, null=True)
#     south = models.CharField(max_length=63, blank=True, null=True)
#     west = models.CharField(max_length=63, blank=True, null=True)
#     north = models.CharField(max_length=63, blank=True, null=True)
#     east_west = models.CharField(max_length=63, blank=True, null=True)
#     north_south = models.CharField(max_length=63, blank=True, null=True)
#     description = models.CharField(max_length=90, blank=True, null=True)
#     original_location = models.CharField(max_length=63, choices=originals)
#     copygbs = models.BooleanField()
#     enclosure = models.CharField(max_length=1000, blank=True, null=True,
#                                  help_text="(Please provide comma separated list of Enclosed Document Number & Names)")
#     remarks = models.CharField(max_length=43, blank=True, null=True)
#     dochyperlink = models.URLField(null=True, blank=True)
#     land_usage = models.CharField(max_length=63, choices=usage)
#     modeofmanagement = models.CharField(max_length=63, choices=management)
#     typeofinstrument = models.CharField(max_length=63, choices=instrument)
#     annaulfees = models.IntegerField(blank=True, null=True)
#     inchargeperson = models.ForeignKey(Member, db_column='inchargeperson', related_name='inchargeperson')
#     specialstatus = models.CharField(max_length=63, choices=status)
#     specialinfoindetails = models.TextField(null=True, blank=True)
#     khata = models.BooleanField()
#     hyperlinkofmutation = models.URLField(null=True, blank=True)
#     geocordinate_eastwest = models.PointField(null=True, blank=True)
#     geocordinate_northsouth = models.PointField(null=True, blank=True)
#
#     class Meta:
#         db_table = 'assetLand'
#
#
# class AssetLandAdmin(admin.ModelAdmin):
#     list_display = ('id', 'inchargeperson', 'areacode', 'original_location', 'description', 'specialstatus')
#     model = AssetLand
#     form = modelform_factory(AssetLand, form=AssetLandForm, fields='__all__')
#     fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': (
#             'areacode', 'doc', 'place', 'donee_vendee', 'regn_no', 'sub_registrar', 'land_type', 'salutation',
#             'donor_vendor', 'relationship', 'relative', 'acrage', 'yards', 'sqmeter', 'survey', 'address', 'state',
#             'value', 'stamp_worth', 'regn_fees', 'total', 'east', 'south', 'west', 'north', 'east_west', 'north_south',
#             'description', 'original_location', 'copygbs', 'enclosure', 'remarks', 'dochyperlink', 'land_usage',
#             'modeofmanagement', 'typeofinstrument', 'annaulfees', 'inchargeperson', 'specialstatus',
#             'specialinfoindetails', 'khata', 'hyperlinkofmutation', 'geocordinate_eastwest', 'geocordinate_northsouth'),
#         }),
#     )
#
#
# class AssetBuilding(BaseModel):
#     status = (('completed', 'Completed'),
#               ('ongoing', 'Ongoing'),
#               ('proposed', 'Proposed'),
#               )
#
#     organisation = models.ForeignKey(Organisation, db_column='organisation', related_name='organisation')
#     code = models.IntegerField(unique=True)
#     description = models.CharField(max_length=65, blank=True, null=True)
#     numberoffloors = models.IntegerField(blank=True, null=True)
#     status = models.CharField(max_length=63, choices=status)
#     plinthareainsft = models.IntegerField(blank=True, null=True)
#     plinthareainsqm = models.IntegerField(blank=True, null=True)
#     estematedcost = models.IntegerField(blank=True, null=True)
#     approvedbyadp = models.BooleanField()
#     foundationdate = models.DateField(blank=True, null=True)
#     # foundationphoto = models.CharField(max_length=127, blank=True, null=True)
#     foundationphoto = models.ImageField(upload_to='img', blank=True, null=True)
#     inaugrationdate = models.DateField(blank=True, null=True)
#     # inaugrationphoto = models.CharField(max_length=127, blank=True, null=True)
#     inaugrationphoto = models.ImageField(upload_to='img', blank=True, null=True)
#     latestrenovation = models.DateField(blank=True, null=True)
#     renovationphoto = models.CharField(max_length=127, blank=True, null=True)
#     maindonors = models.ForeignKey(Member, db_column='maindonors', related_name='maindonors')
#     structuralplan = models.BooleanField()
#     structuralplanurl = models.URLField(blank=True, null=True)
#     sanctioned = models.BooleanField()
#     sanctionplanurl = models.URLField(blank=True, null=True)
#     contractorname = models.CharField(max_length=65, blank=True, null=True)
#     contractoraddress = models.TextField(max_length=250, null=True)
#     contractornumber = models.IntegerField(null=True, blank=True)
#     capitalisedintheaccountof = models.BooleanField()
#     electricalconnectionnumb = models.CharField(max_length=65, blank=True, null=True)
#     sanctionedload = models.IntegerField(blank=True, null=True)
#     currentstate = models.CharField(max_length=15, choices=current_options, default='excellent')
#     maintenrequirementcost = models.IntegerField(blank=True, null=True)
#     compiled = models.CharField(max_length=128, blank=True, null=True)
#
#     class Meta:
#         db_table = 'assetBuilding'
#
#     def save(self):
#         from django.db.models import Max
#         "Get last value of Code and Number from database, and increment before save"
#         if not self.pk:
#             self.code = AssetBuilding.objects.all().aggregate(Max('code'))['code__max']
#             if self.code == None:
#                 self.code = 1
#             else:
#                 self.code += 1
#
#         super(AssetBuilding, self).save()
#
#
# class AssetBuildingAdmin(admin.ModelAdmin):
#     list_display = ('id', 'maindonors', 'code', 'organisation', 'description', 'status')
#
#     model = AssetBuilding
#     form = modelform_factory(AssetBuilding, form=AssetBuildingForm, fields='__all__')
#     fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('organisation', 'maindonors', 'description', 'numberoffloors', 'status', 'plinthareainsft',
#                        'plinthareainsqm',
#                        'estematedcost', 'approvedbyadp', 'foundationdate', 'foundationphoto', 'inaugrationdate',
#                        'inaugrationphoto',
#                        'latestrenovation', 'structuralplan', 'structuralplanurl', 'sanctioned', 'sanctionplanurl',
#                        'contractorname',
#                        'contractoraddress', 'contractornumber', 'capitalisedintheaccountof', 'electricalconnectionnumb',
#                        'sanctionedload', 'currentstate', 'maintenrequirementcost', 'compiled'),
#         }),
#     )
#
#
# class AssetEquipment(models.Model):
#     status = (('installed', 'Installed'),
#               ('proposed', 'Proposed'),
#               )
#
#     organisation = models.ForeignKey(Organisation, db_column='organisation')
#     code = models.IntegerField(unique=True)
#     equipmentdescription = models.CharField(max_length=65, blank=True, null=True)
#     estematedcost = models.IntegerField(blank=True, null=True)
#     equipmentlifeexpectancy = models.IntegerField(blank=True, null=True)
#     status = models.CharField(max_length=63, choices=status)
#     approvedbyadp = models.BooleanField()
#     procurementdate = models.DateField(blank=True, null=True)
#     inaugrationdate = models.DateField(blank=True, null=True)
#     # inaugrationphoto = models.CharField(max_length=127, blank=True, null=True)
#     inaugrationphoto = models.ImageField(upload_to='img', blank=True, null=True)
#     latestupkeep = models.DateField(blank=True, null=True)
#     # latestphoto = models.CharField(max_length=127, blank=True, null=True)
#     latestphoto = models.ImageField(upload_to='img', blank=True, null=True)
#     maindonors = models.ForeignKey(Member, db_column='maindonors')
#     sizedimension1length = models.IntegerField(blank=True, null=True)
#     sizedimension2bredth = models.IntegerField(blank=True, null=True)
#     sizedimension3height = models.IntegerField(blank=True, null=True)
#     installationareasqm = models.IntegerField(blank=True, null=True)
#     government_permission_required = models.BooleanField(default='No')
#     government_permission_letter_url = models.URLField(blank=True, null=True)
#     contractorname = models.CharField(max_length=65, blank=True, null=True)
#     contractoraddress = models.TextField(blank=True, null=True)
#     contractornumber = models.IntegerField(blank=True, null=True)
#     capitalisedintheaccountof = models.BooleanField()
#     requireedload = models.IntegerField(blank=True, null=True)
#     currentstate = models.CharField(max_length=15, choices=current_options, default='excellent')
#     amc = models.BooleanField()
#     amc_expire = models.DateField(blank=True, null=True)
#     amc_worth = models.IntegerField(blank=True, null=True)
#     majormantainenacedue = models.IntegerField(blank=True, null=True)
#     majormantainenacecost = models.IntegerField(blank=True, null=True)
#     compiled = models.CharField(max_length=128, blank=True, null=True)
#
#     class Meta:
#         db_table = 'assetEquipment'
#
#     def save(self):
#         from django.db.models import Max
#         "Get last value of Code and Number from database, and increment before save"
#         if not self.pk:
#             self.code = AssetEquipment.objects.all().aggregate(Max('code'))['code__max']
#             if self.code == None:
#                 self.code = 1
#             else:
#                 self.code += 1
#
#         super(AssetEquipment, self).save()
#
#
# class AssetEquipmentAdmin(admin.ModelAdmin):
#     model = AssetEquipment
#     list_display = ('maindonors', 'code', 'organisation', 'equipmentdescription', 'status')
#     form = modelform_factory(AssetEquipment, form=AssetEquipmentForm, fields='__all__')
#     fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('organisation', 'equipmentdescription', 'estematedcost', 'equipmentlifeexpectancy', 'status',
#                        'approvedbyadp',
#                        'procurementdate', 'government_permission_required',
#                        'inaugrationdate', 'inaugrationphoto', 'latestupkeep', 'latestphoto', 'maindonors',
#                        'sizedimension1length',
#                        'sizedimension2bredth', 'sizedimension3height', 'installationareasqm',
#                        'government_permission_letter_url',
#                        'contractorname', 'contractoraddress', 'capitalisedintheaccountof', 'requireedload',
#                        'currentstate',
#                        'amc', 'amc_expire', 'amc_worth', 'majormantainenacedue', 'majormantainenacecost', 'compiled'),
#         }),
#     )
#
#
# class Trustee(BaseModel):
#     member = models.ForeignKey(Member, db_column="member", related_name="trusteemember")
#     organisation = models.ForeignKey(Organisation, db_column="organisation")
#     designation = models.CharField(max_length=23, blank=True, null=True)
#     department = models.CharField(max_length=35, blank=True, null=True)
#     from_tenure = models.DateField()
#     to_tenure = models.DateField()
#     tenure_active = models.CharField(max_length=15, choices=(('yes', 'yes'), ('no', 'No'),))
#     valid = models.CharField(max_length=15, choices=(('yes', 'Yes'), ('no', 'No'),), default='yes')
#     active = models.CharField(max_length=15, choices=(('yes', 'Yes'), ('no', 'No'),))
#
#     class Meta:
#         db_table = 'trustee'
#
#
# class TrusteeAdmin(admin.ModelAdmin):
#     model = Trustee
#     form = modelform_factory(Trustee, form=TrusteeForm, fields='__all__')
#     fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': (
#             'member', 'organisation', 'designation', 'department', 'from_tenure', 'to_tenure', 'tenure_active', 'valid',
#             'active'),
#         }),
#     )
#
#
# class Honorary(BaseModel):
#     member = models.ForeignKey(Member, db_column="member", related_name="Honoraryemember")
#     designation = models.CharField(max_length=23, blank=True, null=True)
#     department = models.CharField(max_length=35, blank=True, null=True)
#     organisation = models.ForeignKey(Organisation, db_column="organisation")
#     date_of_occasion = models.DateField()
#     occasion = models.CharField(max_length=40, blank=True, null=True)
#     reference = models.CharField(max_length=40, blank=True, null=True)
#     dignitary = models.BooleanField()
#
#     class Meta:
#         db_table = 'honorary'
#
#
# class Complimentary(BaseModel):
#     refered_by = models.TextField()
#     occasion = models.TextField()
#
#     class Meta:
#         db_table = 'complimentary'
#
#
# class MedicalProfileAdmin(admin.ModelAdmin):
#     list_display = ('id', 'mid',)
#     search_fields = ('mid',)
#
#
# class MedicalProfile(BaseModel):
#     mid = models.ForeignKey(Member, unique=True, db_column='mid', related_name='member')
#     height = models.IntegerField()
#     weight = models.IntegerField()
#     diabetes = models.CharField(max_length=255, blank=True, null=True)
#     hypertension = models.CharField(max_length=255, blank=True, null=True)
#     tuberculosis = models.CharField(max_length=255, blank=True, null=True)
#     musculoskeletalproblems = models.CharField(max_length=255, blank=True, null=True)
#     gastrointestinalproblem = models.CharField(max_length=255, blank=True, null=True)
#     renalproblrms = models.CharField(max_length=255, blank=True, null=True)
#     cardiacdiseases = models.CharField(max_length=255, blank=True, null=True)
#     chestdiseases = models.CharField(max_length=255, blank=True, null=True)
#     nervoussystemdisorders = models.CharField(max_length=255, blank=True, null=True)
#     anymajororminorsurgeriesinpast = models.CharField(max_length=255, blank=True, null=True)
#     menstrualproblemsandobstetricalhistory = models.CharField(max_length=255, blank=True, null=True)
#     familyhistory = models.CharField(max_length=255, blank=True, null=True)
#     pulse = models.CharField(max_length=255, blank=True, null=True)
#     bp = models.CharField(max_length=255, blank=True, null=True)
#     rr = models.CharField(max_length=255, blank=True, null=True)
#     temp = models.CharField(max_length=255, blank=True, null=True)
#     pallor = models.CharField(max_length=255, blank=True, null=True)
#     icterus = models.CharField(max_length=255, blank=True, null=True)
#     edema = models.CharField(max_length=255, blank=True, null=True)
#     lnpathy = models.CharField(max_length=255, blank=True, null=True)
#     cyanosis = models.CharField(max_length=255, blank=True, null=True)
#     clubbing = models.CharField(max_length=255, blank=True, null=True)
#     skin = models.CharField(max_length=255, blank=True, null=True)
#     hair = models.CharField(max_length=255, blank=True, null=True)
#     oralcavityteeth = models.CharField(max_length=255, blank=True, null=True)
#     eye = models.CharField(max_length=255, blank=True, null=True)
#     ent = models.CharField(max_length=255, blank=True, null=True)
#     skeletalsystem = models.CharField(max_length=255, blank=True, null=True)
#     cns = models.CharField(max_length=255, blank=True, null=True)
#     cvs = models.CharField(max_length=255, blank=True, null=True)
#     chest = models.CharField(max_length=255, blank=True, null=True)
#     abdomen = models.CharField(max_length=255, blank=True, null=True)
#     genitals = models.CharField(max_length=255, blank=True, null=True)
#     hb = models.CharField(help_text="gm%", max_length=255, blank=True, null=True)
#     tc = models.CharField(help_text="cells/c.mm", max_length=255, blank=True, null=True)
#     dcn = models.CharField(help_text="DC:N-", max_length=255, blank=True, null=True)
#     dcl = models.CharField(help_text="DC:L-", max_length=255, blank=True, null=True)
#     dce = models.CharField(help_text="DC:E-", max_length=255, blank=True, null=True)
#     dcm = models.CharField(help_text="DC:M-", max_length=255, blank=True, null=True)
#     esr = models.CharField(help_text="mm/hr", max_length=255, blank=True, null=True)
#     aec = models.CharField(help_text="cells/c.mm", max_length=255, blank=True, null=True)
#     lipidprofile = models.CharField(max_length=255, blank=True, null=True)
#     vdrl = models.CharField(max_length=255, blank=True, null=True)
#     striglycerides = models.CharField(help_text="mg%", max_length=255, blank=True, null=True)
#     urineanalysis = models.CharField(max_length=255, blank=True, null=True)
#     scholestrol = models.CharField(help_text="s.cholestrol (mg%)", max_length=255, blank=True, null=True)
#     shdl = models.CharField(help_text="s.hdl (mg%)", max_length=255, blank=True, null=True)
#     sldl = models.CharField(help_text="s,ldl (mg%)", max_length=255, blank=True, null=True)
#     svldlmg = models.CharField(help_text="s.vldl (mg%)", max_length=255, blank=True, null=True)
#     thyroidprofile = models.CharField(max_length=255, blank=True, null=True)
#     xray = models.CharField(max_length=255, blank=True, null=True)
#     usg = models.CharField(max_length=255, blank=True, null=True)
#     consultingDoctor = models.ForeignKey(Member, null=False, blank=False, related_name='consultingDoctor')
#     impressioninsummary = models.CharField(max_length=255, blank=True, null=True)
#     indian = models.BooleanField(default=True)
#     dnd_mails = models.BooleanField(default=True)
#     dnd_sms = models.BooleanField(default=True)
#     dnd_emails = models.BooleanField(default=True)
#
#     class Meta:
#         db_table = "medicalProfile"
#
#
# status_options = (('self', 'Self'),
#                   ('working', 'Working'),
#                   ('department', 'Department'),
#                   ('retired', 'Retired'),
#                   )
#
#
# class StaffProfile(BaseModel):
#     status = models.CharField(max_length=65, choices=status_options)
#     mid = models.ForeignKey(Member, db_column='mid', related_name='memberstaff')
#     fbid = models.CharField(max_length=255, blank=True, null=True)
#     gender = models.CharField(max_length=1, choices=gender_options, default='D')
#     duty = models.CharField(max_length=255, blank=True, null=True)
#     department = models.CharField(max_length=255, blank=True, null=True)
#     knowssriswamijisince = models.IntegerField(blank=True, null=True)
#     martialstatus = models.CharField(max_length=7, choices=martialstatus_options, default='single')
#     spousename = models.ForeignKey(Member, db_column='spousename', related_name='spousename')
#     residentspouse = models.BooleanField(default=True)
#     father = models.ForeignKey(Member, db_column='father', blank=True, null=True, related_name='father')
#     mother = models.ForeignKey(Member, db_column='mother', blank=True, null=True, related_name='mother')
#     children = models.ForeignKey(Member, db_column='children', blank=True, null=True, related_name='children')
#     introducer = models.ForeignKey(Member, db_column='introducer', blank=True, null=True, related_name='introducer')
#     contacts = models.ForeignKey(Member, db_column='contacts', blank=True, null=True, related_name='contacts')
#     dateofjoining = models.DateField(blank=True, null=True)
#     dateofregistration = models.DateTimeField(blank=True, null=True)
#     note = models.CharField(max_length=255, blank=True, null=True)
#     headofthefamily = models.BooleanField(default=True)
#
#     class Meta:
#         db_table = "staffProfile"
#
#
# class StaffProfileAdmin(ExportMixin, admin.ModelAdmin):
#     list_display = ('id', 'mid', 'gender', 'department')
#     # list_filter = ('mid')
#     # search_fields = ('mid')
#     model = Member
#     form = modelform_factory(StaffProfile, form=StaffForm, fields='__all__')
#     fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': (
#                 'mid',
#                 'fbid',
#                 'gender',
#                 'duty',
#                 'department',
#                 'knowssriswamijisince',
#                 'martialstatus',
#                 'spousename',
#                 'residentspouse',
#                 'father',
#                 'mother',
#                 'children',
#                 'introducer',
#                 'contacts',
#                 'dateofjoining',
#                 'note',
#                 'headofthefamily',
#             )
#         }),
#     )
#
#
# class Event(BaseModel):
#     event_date = models.DateField()
#     seva = models.ForeignKey(Seva)
#     status = models.SmallIntegerField(choices=status_choices, default=BOOLEAN_YES)
#
#     class Meta:
#         unique_together = ('event_date', 'seva')
#
# class Relatives(BaseModel):
#     member = models.ForeignKey(Member, db_column='mid', unique=True, related_name='self')
#     relative_type = models.CharField(max_length=9, choices=relativetype_choices, default = 'friend')
#     relativemember = models.ForeignKey(Member, db_column='relativemember', blank=True, null=True, related_name='relativemember')
#     class Meta:
#         db_table = "Relatives"
#
# class RelativesAdmin(admin.ModelAdmin):
#     list_display = ('id', 'member')
