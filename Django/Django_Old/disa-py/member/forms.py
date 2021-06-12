from django.utils.html import escapejs, format_html
from django.forms.widgets import RadioSelect
from django import forms
from django.forms import ModelForm
from django.utils.safestring import mark_safe
from django.db import connection


relativetype_choices=( ('friend','Friend'),
                       ('wife','Wife'),
                       ('husband','Husband'),
                       ('father','Father'),
                       ('mother','Mother'),
                       ('sister','Sister'),
                       ('brother','Brother'),
                       ('son','Son'), 
                       ('daughter','Daughter'),
                       ('Cousin','Cousin'),
                       ('inlaws','Inlaws'),
                       ('wellwisher','Wellwisher'),
                       ('guru','Guru')
                     )


gender_options = ( ('m','Male'),
                   ('f','Female'),
                   ('d','Data Not Available')
                 )

calendar_options = ( ('lunar','Lunar'),
                     ('solar','Solar'),
                     ('default','Default')
                   )
martialstatus_options =( ('single','Single'),
                         ('married','Married'),
                       )

current_options = (('excellent', 'Excellent'),
                       ('good', 'Good'),
                       ('poor', 'Poor'),
                       ('urgentrepair', 'UrgentRepair'),
                       ('abandon', 'Abandon'),
                      )

states = (('Andhra Pradesh', 'Andhra Pradesh'),
          ('Arunachal Pradesh', 'Arunachal Pradesh'),
          ('Assam', 'Assam'),
          ('Bihar', 'Bihar'),
          ('Chhatisgarh', 'Chhattisgarh'),
          ('Goa', 'Goa'),
          ('Gujarat', 'Gujarat'),
          ('Haryana', 'Haryana'),
          ('Himachal Pradesh', 'Himachal Pradesh'),
          ('Jammu & Kashmir', 'Jammu & Kashmir'),
          ('Jharkhand', 'Jharkhand'),
          ('Karnataka', 'Karnataka'),
          ('Kerala', 'Kerala'),
          ('Madhya Pradesh', 'Madhya Pradesh'),
          ('Maharashtra', 'Maharashtra'),
          ('Manipur', 'Manipur'),
          ('Meghalaya', 'Meghalaya'),
          ('Mizoram', 'Mizoram'),
          ('Nagaland', 'Nagaland'),
          ('Odisa', 'Odisha (Orissa)'),
          ('Punjab', 'Punjab'),
          ('Rajasthan', 'Rajasthan'),
          ('Sikkim', 'Sikkim'),
          ('Tamil Nadu', 'Tamil Nadu'),
          ('Telangana', 'Telangana'),
          ('Tripura', 'Tripura'),
          ('Uttar Pradesh', 'Uttar Pradesh'),
          ('Uttarakhand', 'Uttarakhand'),
          ('West Bengal', 'West Bengal'),
         )

Land_Type = (('gift', 'Gift'),
             ('sale', 'Sale'),
             ('lease', 'Lease'),
             ('will', 'Will'),
             ('exchange', 'Exchange'),
             ('license', 'Licenses'),
             ('allotment', 'Allotment'),
            )

slt_type = (('smt', 'Smt'),
            ('sri', 'Sri'),
            ('kumari', 'Kumari'),
            ('messers', 'Messers'),
           )

relation_type = (('son', 'Son'),
                 ('daughter', 'Daughter'),
                 ('wife', 'Wife'),
                )

originals = (('adp', 'ADP'),
              ('gbs', 'GBS'),
              ('vendor', 'Vendor/ Donor'),
             )

usage = (('agriculture', 'Agriculture'),
         ('ashrama', 'Ashrama'),
         ('commercial', 'Commercial'),
         ('residential', 'Residential'),
         ('redundant', 'Redundant'),
         ('disputed', 'Disputed'),
        )

management = (('self', 'Self'),
              ('trust', 'Affiliated_Trust'),
              ('person', 'Affiliated_Person'),
             )

instrument = (('license', 'License'),
              ('lease', 'Lease'),
              ('informal', 'Informal'),
             )

status = (('dispute', 'Dispute'),
          ('disposal', 'Disposal'),
          ('aquisition', 'Acquisition'),
         )

class HorizRadioRenderer(forms.RadioSelect.renderer):
    """ this overrides widget method to put radio buttons horizontally
        instead of vertically.
    """
    def render(self):
            """Outputs radios"""
            return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

class MemberForm(forms.ModelForm):
     def __init__(self,*args,**kwargs):
          super(MemberForm,self).__init__(*args,**kwargs)
          self.fields['gender'].widget = RadioSelect(renderer=HorizRadioRenderer, choices=gender_options)
          self.fields['gender'].value='d'
          self.fields['calendar_type'].widget = RadioSelect(renderer=HorizRadioRenderer, choices=calendar_options)
          self.fields['calendar_type'].value='default'

          self.fields['maasam'].empty_label = "--Select Maasam--"
          self.fields['paksham'].empty_label = "--Select Paksham--"
          self.fields['tithi'].empty_label = "--Select Tithi--"
          self.fields['rasi'].empty_label = "--Select Raasi--"
          self.fields['nakshatram'].empty_label = "--Select Nakshatram--"


class SevaForm(forms.ModelForm):
     def __init__(self,*args,**kwargs):
          super(SevaForm,self).__init__(*args,**kwargs)
          self.fields['calendar_type'].widget = RadioSelect(renderer=HorizRadioRenderer, choices=calendar_options)
          self.fields['calendar_type'].value='default'

          self.fields['maasam'].empty_label = "--Select Maasam--"
          self.fields['paksham'].empty_label = "--Select Paksham--"
          self.fields['tithi'].empty_label = "--Select Tithi--"
          self.fields['raasi'].empty_label = "--Select Raasi--"
          self.fields['nakshatram'].empty_label = "--Select Nakshatram--"

class AssetLandForm(forms.ModelForm):
     def __init__(self,*args,**kwargs):
          super(AssetLandForm,self).__init__(*args,**kwargs)
          self.fields['address'].widget.attrs['cols']= 10
          self.fields['address'].widget.attrs['rows'] = 5
          self.fields['specialinfoindetails'].widget.attrs['cols']= 10
          self.fields['specialinfoindetails'].widget.attrs['rows'] = 5

class AssetBuildingForm(forms.ModelForm):
     def __init__(self,*args,**kwargs):
          super(AssetBuildingForm,self).__init__(*args,**kwargs)
          self.fields['currentstate'].widget = RadioSelect(renderer=HorizRadioRenderer, choices=current_options)

class AssetEquipmentForm(forms.ModelForm):
     def __init__(self,*args,**kwargs):
          super(AssetEquipmentForm,self).__init__(*args,**kwargs)
          self.fields['currentstate'].widget = RadioSelect(renderer=HorizRadioRenderer, choices=current_options)

class TrusteeForm(forms.ModelForm):
     def __init__(self,*args,**kwargs):
          super(TrusteeForm,self).__init__(*args,**kwargs)
          self.fields['tenure_active'].widget = RadioSelect(renderer=HorizRadioRenderer, choices=(('yes', 'Yes'),('no','No'),))
          self.fields['valid'].widget = RadioSelect(renderer=HorizRadioRenderer, choices=(('yes','Yes'),('no', 'No'),))
          self.fields['active'].widget = RadioSelect(renderer=HorizRadioRenderer, choices=(('yes','Yes'),('no', 'No'),))


select_mode = ( ('all','All'),
                ('group','Group'),
                ('others','Others')
              )
select_month = ( ('01', 'January'),
                 ('02', 'February'),
                 ('03', 'March'),
                 ('04', 'April'),
                 ('05', 'May'),
                 ('06', 'June'),
                 ('07', 'July'),
                 ('08', 'August'),
                 ('09', 'September'),
                 ('10', 'October'),
                 ('11', 'November'),
                 ('12', 'December')
               )

class EmailForm(forms.Form):

    cur = connection.cursor()
    group_choices =  []
    group_list = []


    mode = forms.TypedChoiceField(choices=select_mode, widget=forms.RadioSelect(renderer=HorizRadioRenderer), initial = 'others')
    query = "Select name from sevaCategories;"
    cur.execute(query)
    group_choices = cur.fetchall()

    for each in group_choices:
        tmp = (each[0], each[0])
        group_list.append(tmp)

    cur.close()

    groups = forms.TypedChoiceField(choices=tuple(group_list), required=False)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def __init__(self, *args, **kwargs):
        super(EmailForm, self).__init__(*args, **kwargs)
        grouplist = []
        cur = connection.cursor()
        query = "select name from groupNames;"
        cur.execute(query)
        groupchoices = cur.fetchall()
        cur.close()
        for each in groupchoices:
           tmp = (each[0], each[0])
           grouplist.append(tmp)
        # Add select option to the typedchoice field
        self.fields['groups'].choices =[("","--Select Group--")] + grouplist + list(self.fields['groups'].choices)[1:]


class SmsForm(forms.Form):

    cur = connection.cursor()
    group_choices = []
    group_list = []

    mode = forms.TypedChoiceField(choices=select_mode, widget=forms.RadioSelect(renderer=HorizRadioRenderer), initial = 'others')
    query = "Select name from sevaCategories;"
    cur.execute(query)
    group_choices = cur.fetchall()
    cur.close()

    for each in group_choices:
        tmp = (each[0],each[0])
        group_list.append(tmp)

    groups = forms.TypedChoiceField(choices=tuple(group_list), required=False)

    message = forms.CharField(widget=forms.Textarea(attrs={'id':'template_msg_preview','class':'data-promotional'}), required=True)

    def __init__(self, *args, **kwargs):
        super(SmsForm, self).__init__(*args, **kwargs)
        cur = connection.cursor()
        grouplist = []
        query = "select name from groupNames;"
        cur.execute(query)
        groupchoices = cur.fetchall()
        cur.close()

        for each in groupchoices:
           tmp = (each[0], each[0])
           grouplist.append(tmp)
        self.fields['groups'].choices=[("","--Select Group--")] + grouplist + list(self.fields['groups'].choices)[1:]

mode = ( ('lunar', 'Lunar'),
         ('default', 'Default')
       )

class ReportsForm(forms.Form):

    cur = connection.cursor()
    lunarmasam_list = []
    lunarmasam_choices = []

    group_choices = []
    group_list = []


    query = "Select maasam from maasamTypes;"
    cur.execute(query)
    lunarmasam_choices = cur.fetchall()

    for each in lunarmasam_choices:
        tmp = (each[0],each[0])
        lunarmasam_list.append(tmp)

    mode = forms.TypedChoiceField(choices=mode, widget=forms.RadioSelect(renderer=HorizRadioRenderer), initial = 'default')

    lunarMasam = forms.TypedChoiceField(choices=tuple(lunarmasam_list), required=False)

    months = forms.TypedChoiceField(choices=select_month, required=False)

    query = "Select name from sevaCategories;"
    cur.execute(query)
    group_choices = cur.fetchall()

    cur.close()

    for each in group_choices:
        tmp = (each[0],each[0])
        group_list.append(tmp)

    seva_category = forms.TypedChoiceField(choices=tuple(group_list))

    def __init__(self, *args, **kwargs):
        super(ReportsForm, self).__init__(*args, **kwargs)
        self.fields['lunarMasam'].choices=[("","--Select Lunar Masam--")] + list(self.fields['lunarMasam'].choices)[1:]
        self.fields['seva_category'].choices=[("","--Select Seva Categories--")] + list(self.fields['seva_category'].choices)[1:]
        self.fields['months'].choices=[("","--Select Month--")] + list(self.fields['months'].choices)

class StaffForm(forms.ModelForm):
     def __init__(self,*args,**kwargs):
          super(StaffForm,self).__init__(*args,**kwargs)
          self.fields['gender'].widget = RadioSelect(renderer=HorizRadioRenderer, choices=gender_options)
          self.fields['gender'].value='d'
          self.fields['martialstatus'].widget = RadioSelect(renderer=HorizRadioRenderer, choices=martialstatus_options)
          self.fields['martialstatus'].value='single'


class Relatives(forms.ModelForm):
     def __init__(self,*args,**kwargs):
          self.fields['relativetype'].choices=[("","--Select relativetype--")] +list(self.fields['relativetype'].choices)

