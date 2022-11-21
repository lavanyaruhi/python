import re
str='HelloHIfriendsHappy23YangNayhi@!'
print("no. of uppercase chars: ",len(re.findall(r"[A-Z]",str)))
print("no. of lowercase chars: ",len(re.findall(r"[a-b]",str)))
print("no. of numeric chars: ",len(re.findall(r"[0-9]",str)))
print("no. of special chars: ",len(re.findall(r"[,.!?@$%^&*();:']",str)))
