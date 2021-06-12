from django.db import connection
from django.conf import settings
from django.template.loader import get_template
from django.template import Context
from member.email import sendmassmail
from member.sms import sendmass_SMS
from django.template.loader import render_to_string
import time, datetime
from datetime import timedelta
from member.models import  Seva, SevaCategory, Member, Address

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    '''
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ] '''
    for row in cursor.fetchall():
       yield  dict(zip(columns, row))

#Sends puja intimation mail and sms to the members on the same day. Executed once in a day
def PujaIntimation():

    today_date = time.strftime("%m%d")
    query_param = {'sevaday__icontains': today_date}
    seva_list = Seva.objects.filter(**query_param)

    subject = 'Puja Intimation'
    datatuples = []
    sms_datatuples = []
    
    for seva in seva_list:
        member = seva.mid
        if member.salutation:
            salutation = member.salutation
        else:
            salutation = ''
        message_html = get_template('puja.html').render(
            Context({
                'member_slt':salutation,
                'member_name':member.name,
                'seva_type': seva.sid.name
            })
        )
        number = member.mobile
        message_sms = str(render_to_string('puja.txt')).format(name=salutation+' '+member.name)
        #(subject, text_content, html_content, from_email, recipient_list)
        datatuples.append((subject, None, message_html, settings.DEFAULT_FROM_EMAIL, [member.email]))
        sms_datatuples.append((number, message_sms))

    sendmassmail(datatuples)
    sendmass_SMS(sms_datatuples)

#Sends puja intimation mail and sms to the members two days before. Executed once in a day
def AdvancedPujaIntimation():
    
    timeNow = datetime.datetime.now()
    pujaTime = timeNow + datetime.timedelta(days=2)
    
    sevaday = pujaTime.strftime("%m%d")
    query_param = {'sevaday__icontains': sevaday}
    seva_list = Seva.objects.filter(**query_param)

    subject = 'Advance Puja Intimation'
    datatuples = []
    sms_datatuples = []
    
    for seva in seva_list:
        member = seva.mid
        if member.salutation:
            salutation = member.salutation
        else:
            salutation = ''
        message_html = get_template('AdvancePuja.html').render(
            Context({
                'member_slt':salutation,
                'member_name':member.name,
                'seva_date' : seva.sevaday,
                'seva_name' : seva.sid.name
            })
        )
        number = member.mobile
        message_sms = str(render_to_string('AdvancePuja.txt')).format(name=salutation+' '+member.name, date=seva.sevaday, seva_name=seva.sid.name)
        #(subject, text_content, html_content, from_email, recipient_list)
        datatuples.append((subject, None, message_html, settings.DEFAULT_FROM_EMAIL, [member.email]))
        sms_datatuples.append((number, message_sms))

    sendmassmail(datatuples)
    sendmass_SMS(sms_datatuples)

#Sends prasadam dispatch mail and SMS to the members. Executed once in a day
def PrasadamDispatchIntimation():

    timeNow = datetime.datetime.now()
    pujaTime = timeNow + datetime.timedelta(days=-1)
    
    sevaday = pujaTime.strftime("%m%d")
    query_param = {'sevaday__icontains': sevaday}
    seva_list = Seva.objects.filter(**query_param)
    subject = 'Prasadam Dispatch Intimation'
    datatuples = []
    sms_datatuples = []

    for seva in seva_list:

        member = seva.mid
        if member.salutation:
            salutation = member.salutation
        else:
            salutation = ''
        
        message_html = get_template('prasadamDispatch.html').render(
            Context({
                'member_slt':salutation,
                'member_name':member.name,
                'member_mobile' :member.mobile
            })
        )
       
        message_html = None
        number = member.mobile
        message_sms = str(render_to_string('prasadamDispatch.txt')).format(name=salutation+' '+member.name)
        #(subject, text_content, html_content, from_email, recipient_list)
        datatuples.append((subject, None, message_html, settings.DEFAULT_FROM_EMAIL, [member.email]))
        sms_datatuples.append((number, message_sms))

    sendmassmail(datatuples)
    sendmass_SMS(sms_datatuples)

#Sends annual reminder mail and SMS to all the members and this will be executed once in a year
def AnnualReminder():
   
    members = Member.objects.all()

    subject = 'Annual Reminder'
    datatuples = []
    sms_datatuples = []

    for member in members:
        if member.salutation:
            salutation = member.salutation
        else:
            salutation = ''
        
        if member.surname:
            surname = member.surname
        else:
            surname = ''

        message_html = get_template('AnnualReminder.html').render(
            Context({
                'member_slt':salutation,
                'member_surname':surname,
                'member_name':member.name,
                'member_mobile' :member.mobile
            })
        )
        number = member.mobile
        message_sms = str(render_to_string('AnnualReminder.txt')).format(name=salutation+' '+member.name)
        #(subject, text_content, html_content, from_email, recipient_list)
        datatuples.append((subject, None, message_html, settings.DEFAULT_FROM_EMAIL, [member.email]))
        sms_datatuples.append((number, message_sms))

    sendmassmail(datatuples)
    sendmass_SMS(sms_datatuples)

    
