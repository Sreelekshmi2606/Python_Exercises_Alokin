def case(string_1):
    d={'upper':0,'lower':0}
    for i in string_1:
        if i.isupper():
            d['upper']+=1
        elif i.islower():
            d["lower"]+=1
        else:
           pass
    print ("Original String : ", string_1)
    print ("No. of Upper case characters : ", d["upper"])
    print ("No. of Lower case Characters : ", d["lower"])

case('HeLlo')
