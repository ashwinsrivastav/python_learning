s = "A man, a plan, a canal: Panama"
c=""
for i in s.lower():
    if i.isalnum():
       c=c+i
if c==c[::-1]:
    print("true")