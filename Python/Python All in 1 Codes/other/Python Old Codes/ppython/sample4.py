import System, System.Net, sys, clr
from System.Net import *
import System.IO

url = 'https://b2bqa.amat.com/receiveQuoteFromCPQDEV'
url1 = 'https://b2bqa.amat.com/receiveQuoteFromCPQDEV/LogIn?username=intg-cpquser&password=cpquser&domain=APPLIEDMATERIALS_TST'
final_data1 = '<root><customer>roy</customer></root>'
#RestClient.GetBasicAuthenticationHeader('intg-cpquser', 'cpquser')
try:
    webclient = System.Net.WebClient()
    response = webclient.UploadString(url,final_data1)
    #Trace.Write("response-------------->"+str(response))
    print("response-------------->"+str(response))
except System.Net.WebException, e:
    if e.Response is not None:
        streamR = StreamReader(e.Response.GetResponseStream())
        #Trace.Write(streamR.ReadToEnd())
        streamR.Close()
        webclient = System.Net.WebClient()
        response = webclient.UploadString(url1, final_data1)
        print("response-------------->" + str(response))