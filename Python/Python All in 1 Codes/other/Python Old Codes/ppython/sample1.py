import re

s = "<StrongName><![CDATA[ZZ_Billing_Cycle]]></StrongName><Content><![CDATA[Quarterly]]></Content>"
r = "<StrongName><![CDATA[ZZ_Billing_Cycle]]></StrongName><Content><![CDATA[01]]></Content></Content>"

pattern = '<![CDATA[ZZ_Billing_Cycle]]></StrongName><Content><![CDATA['+'Quarterly'+']]>'

a = s.replace(pattern,"<![CDATA[ZZ_Billing_Cycle]]></StrongName><Content><![CDATA["+"01"+"]]></Content>")
print a