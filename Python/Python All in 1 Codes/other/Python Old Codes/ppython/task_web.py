from System.Net import WebRequest
from System.IO import StreamReader
from System.Text import Encoding

def UrlOpen(uri, parameters=None):
    request = WebRequest.Create(uri)
    if parameters is not None:
        request.ContentType = "application/x-www-form-urlencoded"
        #request.Method = "POST" #work for post
        request.Method = "GET"   #not work for get method
        bytes = Encoding.ASCII.GetBytes(parameters)
        request.ContentLength = bytes.Length
        reqStream = request.GetRequestStream()
        reqStream.Write(bytes, 0, bytes.Length)
        reqStream.Close()

    response = request.GetResponse()
    result = StreamReader(response.GetResponseStream()).ReadToEnd()
    return result

#print(UrlOpen("http://localhost:89/api/","data=1"))