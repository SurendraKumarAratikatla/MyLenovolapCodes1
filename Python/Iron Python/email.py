#ScriptExecutor.Execute("MailNotify", {'Mail_Content':a_content})
clr.AddReference('System.Net')
from System.Net import CookieContainer, NetworkCredential
from System.Net.Mail import SmtpClient, MailAddress, Attachment, MailMessage

#a_content = Product.Attributes.GetByName('Email Note').GetValue()
a_content = Quote.GetCustomField('ZZ_PaymentTerms').Content
mailClient = SmtpClient()
#Set the host and port (eg. smtp.gmail.com)
mailClient.Host = "smtp.gmail.com"
mailClient.Port = 587
mailClient.EnableSsl = "true"
#Setup NetworkCredential
mailCred = NetworkCredential()
mailCred.UserName = "surendra.aratikatla@knacksystems.com"
mailCred.Password = "Chinna@30"
mailClient.Credentials = mailCred
#Create two mail adresses, one for send from and the another for recipient
toEmail = MailAddress("surendra.aratikatla@knacksystems.com")
fromEmail = MailAddress("girinath.burri@knacksystems.com")
#Create new MailMessage object
msg = MailMessage(fromEmail,toEmail)
#Set message subject and body
msg.Subject = "PaymentTerms"
msg.Body = a_content
mailClient.Send(msg)