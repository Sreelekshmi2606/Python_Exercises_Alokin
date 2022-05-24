import re
no= '123-456'
x=re.findall(r"[\d]{3}-[\d]{3}-[\d]{3}", no)
print(x)
if x:
    print('Validated')
else:
    print('Not validated')