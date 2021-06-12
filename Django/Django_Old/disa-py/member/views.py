# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
reload(sys)
sys.setdefaultencoding("utf8")

from django.views.generic import TemplateView
from rest_framework import viewsets
from django.conf import settings
from django.core.mail import EmailMessage
from django.db import connection
from django.template.engine import _context_instance_undefined
from member.models import Member,  Seva, Address, SevaCategory, NakshatramType, Organisation
from member.serializers import MemberSerializer, SevaCategorySerializer, NakshatramSerializer, \
    OrganisationSerilalizer, MemberSevaSerializer
# Create your views here.

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework.renderers import JSONRenderer
from django.template.loader import render_to_string
from rolepermissions.decorators import has_role_decorator, has_permission_decorator
from django.contrib.auth import get_user_model
User = get_user_model()

@method_decorator(login_required, name='dispatch')
class MemberHomeView(TemplateView):

    template_name = "member/member.html"

    http_method_names = ['get']

    def get_context_data(self, **kwargs):
        context = super(MemberHomeView, self).get_context_data(**kwargs)
        seva_category_serializer = SevaCategorySerializer(SevaCategory.objects.all(), many=True)
        nakshatram_serializer = NakshatramSerializer(NakshatramType.objects.all(), many=True)
        organisation_serializer = OrganisationSerilalizer(Organisation.objects.all(), many=True)

        context['seva_category_collection'] = JSONRenderer().render(seva_category_serializer.data)
        context['nakshatram_collection'] = JSONRenderer().render(nakshatram_serializer.data)
        context['organisation_collection'] = JSONRenderer().render(organisation_serializer.data)

        return context


@method_decorator(login_required, name='dispatch')
class MemberViewSet(viewsets.ModelViewSet):
    empty_queryset = Member.objects.none()
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def list(self, request, *args, **kwargs):

        queryset = Member.objects
        query_params = request.query_params

        # Flag to check if query was filtered at all.
        filtered = None
        q = query_params.get('q', None)
        if q:
            filtered = True
            queryset = queryset.filter(search__icontains=q)

        name = query_params.get('name', None)
        if name:
            filtered = True
            queryset = queryset.filter(name__icontains=name)

        surname = query_params.get('surname', None)
        if surname:
            filtered = True
            queryset = queryset.filter(surname__icontains=surname)

        mid = query_params.get('mid', None)
        if mid:
            filtered = True
            queryset = queryset.filter(mid=mid)

        place = query_params.get('place', None)
        if place:
            filtered = True
            queryset = queryset.filter(place__icontains=place)

        email = query_params.get('email', None)
        if email:
            filtered = True
            queryset = queryset.filter(email__icontains=email)

        mobile = query_params.get('mobile', None)
        if mobile:
            filtered = True
            queryset = queryset.filter(mobile__icontains=mobile)

        phone = query_params.get('phone', None)
        if phone:
            filtered = True
            queryset = queryset.filter(phone__icontains=phone)

        self.queryset = queryset
        if not filtered:
            self.queryset = self.empty_queryset

        return super(MemberViewSet, self).list(self, request, args, kwargs)

    def retrieve(self, request, *args, **kwargs):
        query_params = request.query_params
        subscriptions = query_params.get('subscriptions', None)
        if subscriptions:
            # Subscriptions are also asked. Hence use Member  seva serialiser
            # which also returns sevas
            self.serializer_class = MemberSevaSerializer

        return super(MemberViewSet, self).retrieve(self, request, args, kwargs)
from django.core.mail import send_mail, BadHeaderError
from .forms import EmailForm, SmsForm, ReportsForm 
from member.sms import Broadcast_SMS
from django.views.generic import TemplateView
from django.shortcuts import redirect, render, render_to_response
from django.template import RequestContext
from disa.middleware.current_user import get_current_user

@method_decorator(login_required, name="get")
class CustomEmail(TemplateView):
    template_name = "email_form.html"

    @method_decorator(has_permission_decorator("SEND_CUSTOM_MESSAGE"))
    def get(self, request, *args, **kwargs):
        form = EmailForm()
        return render(request, self.template_name, {'form': form})

    @method_decorator(has_permission_decorator("SEND_CUSTOM_MESSAGE"))
    def post(self, request, *args, **kwargs):
        form = EmailForm(request.POST, request.FILES)
        # Read the content from the form if the form is valid
        if form.is_valid():
            recipient_list = []
            bcc_list = []
            cc_list = []

            # Read the required fields from the form
            group = form.cleaned_data['groups']
            mode = form.cleaned_data['mode']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            attachment = request.FILES.getlist('attachment')
            cc_list = request.POST.getlist('cc_list')
            cc_list = cc_list[0].split(",")
            
            # If mode is other than others get the recipient_list from database
            if mode == 'others':
                recipient_list = request.POST.getlist('recipient_list')
                recipient_list = recipient_list[0].split(",")

            #In case of sending mails to groups obtained from data base add the recipient list to bcc
            #to avoid sharing of email ids
            else:
                bcc_list = self.GetRecipientList(mode, group)
                bcc_list = bcc_list[0].split(",")

            #In case of others bcc_list is null, in order to send mails to recipient_list max() is introduced 
            for count in xrange(0, max(len(bcc_list),1), settings.MAX_RECIPIENTS):
                email = EmailMessage(to = recipient_list, from_email =
                settings.DEFAULT_FROM_EMAIL, bcc = bcc_list[count:count+settings.MAX_RECIPIENTS], cc = cc_list, body = message, subject = subject)
                if attachment:
                    for eachAttachment in attachment:
                        file = eachAttachment
                        if hasattr(file, 'path'):
                            email.attach_file(file.path)
                        else:
                            email.attach(file.name, file.read())
                try:
                    email.send(fail_silently=False)
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')

            return render_to_response('email_response.html',context_instance=RequestContext(request))

        return redirect('email')

    ''' Gets recipientList from database based on the mode and group '''
    def GetRecipientList(self, mode, group):
        cur = connection.cursor()
        query = "Select name from sevaCategories;"

        if mode == 'all':
            query = 'Select email from members'
        elif mode == 'group':
            try:
                query = 'select id from sevaCategories where name='+" '"+group+" '"
                cur.execute(query)
                sid = cur.fetchone()[0]
                query = "select email from members, sevas where sevas.sid="+ " '"+sid+ " '"+ "AND sevas.mid=members.id";
            except:
                query = 'select id from groupNames where name='+" '"+group+" '"
                cur.execute(query)
                gid = cur.fetchone()[0]
                query = "select email from groupData where gid="+ " '"+gid+ " '"


        cur.execute(query)
        recipient_list = cur.fetchall()
        cur.close()
        return [','.join([each[0] for each in recipient_list])]



@method_decorator(login_required, name="get")
class CustomSms(TemplateView):
    template_name = "sms_form.html"

    @method_decorator(has_permission_decorator("SEND_CUSTOM_MESSAGE"))
    def get(self, request, *args, **kwargs):
        form = SmsForm()
        return render(request,self.template_name, {'form': form})

    @method_decorator(has_permission_decorator("SEND_CUSTOM_MESSAGE"))
    def post(self, request, *args, **kwargs):
        form = SmsForm(request.POST)
        
        if form.is_valid():
            group = form.cleaned_data['groups']
            mode = form.cleaned_data['mode']
            message_sms = form.cleaned_data['message']
            number_list = []
            message = str(render_to_string('customsms.txt')).format(message=message_sms)

           # If mode is other than others get the recipient_list from database
            if mode == 'others':
                number_list = request.POST.getlist('number_list')[0].split(",")
                try:
                    sms = Broadcast_SMS(number_list, message)
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')

            else:
                groupAll_list = self.GetNumberList(mode, group)
                groupAll_list = groupAll_list[0].split(",")
                for count in xrange(0, len(groupAll_list), 20):
                    try:
                        sms = Broadcast_SMS(groupAll_list[count:count+20], message)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                
            return render_to_response('sms_response.html',context_instance=RequestContext(request))

        return redirect('sms')

    ''' Gets numberList from database based on the mode and group '''
    def GetNumberList(self, mode, group):
        cur = connection.cursor()
        query = "Select name from sevaCategories;"

        if mode == 'all':
            query = 'Select mobile from members'
        elif mode == 'group':
            try:
                query = 'select id from sevaCategories where name='+" '"+group+" '"
                cur.execute(query)
                sid = cur.fetchone()[0]
                query = "select mobile from members, sevas where sevas.sid="+ " '"+sid+ " '"+ "AND sevas.mid=members.id";
            except:
                query = 'select id from groupNames where name='+" '"+group+" '"
                cur.execute(query)
                gid = cur.fetchone()[0]
                query = "select mobile from groupData where gid="+ " '"+gid+ " '"


        cur.execute(query)
        number_list = cur.fetchall()
        cur.close()
        return [','.join([each[0] for each in number_list])]


@method_decorator(login_required, name="get")
class Reports(TemplateView):
    template_name = "sevaReports.html"

