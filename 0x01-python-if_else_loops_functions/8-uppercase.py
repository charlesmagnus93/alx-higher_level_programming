#!/usr/bin/python3
def uppercase(str):
    a = ''
    for i in str:
        if (i.isnumeric()):
            a+= i
            continue
        if (ord(i) >= 65 and ord(i)<= 91):
            a+= i
            continue
        b = ord(i) - 32
        a+= f'{chr(b)}'
    
    print(a.format())
