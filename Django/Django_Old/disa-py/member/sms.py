import urllib
import urllib2
from django.conf import settings


'''Send SMS through SMSc.biz url by giving username, password ,number and message'''

def send_SMS(number, message):
    url = settings.SMS_GATEWAY_URL.format(settings.SMS_GATEWAY_USER, settings.SMS_GATEWAY_PASSWORD, number)+message
    response = urllib.urlopen(url)
    result = response.read()

''' Sends different messages to different mobile numbers '''
def sendmass_SMS(datatuple):

    for number, message in datatuple:
        send_SMS(number,message)

''' Broadcast same message to multiple mobile numbers '''
def Broadcast_SMS(numberlist, message):

    for number in numberlist:
        send_SMS(number,message)

