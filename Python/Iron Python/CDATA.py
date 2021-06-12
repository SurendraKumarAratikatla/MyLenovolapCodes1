import re
s = "<EffectiveDate><![CDATA[10/16/19]]></EffectiveDate><DateModified>10/24/19</DateModified><SubCartId><![CDATA[0]]></SubCartId><SubOwnerId><![CDATA[0]]></SubOwnerId><ActiveRevision><![CDATA[1]]></ActiveRevision>"
pattern = "<![CDATA["
pattern2 = "]]>"

#a = re.sub(pattern,'yes',s)

a = s.replace(pattern,"")
p = a.replace(pattern2,"")
print p
