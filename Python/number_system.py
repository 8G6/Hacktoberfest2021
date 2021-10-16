
#Decimal to Octal using inbuit function
def octal_inbuit(a):
    return oct(a)[2:]

#Decimal to Hexadecimal using inbuit function
def hex_inbuit(a):
    return hex(a)[2:]

#Decimal to Octal in the old way
def octal(a):
    s=[]
    while a>0:
        #storing the reminder when diving with 8
        s.append(a%8)
        a=a//8
    #reversing convering to string and joining as a string converting it to int 
    return int("".join([str(i) for i in s[::-1]]))

#Decimal to Hexadecimal in the old way
def hexadec(a):
    s=[]
    while a>0:
        s.append(a%16)
        a=a//16
    for i in range(len(s)):
        if s[i]>9:
            s[i]=chr(s[i]+55)
        else:
            s[i]=str(s[i])
    return "".join(s[::-1])

#Octal to decimal
def octal_to_decimal(a):
    a=list(str(a))
    dec=0
    a=a[::-1]
    #converting octal to decimal
    for i in range(len(a)):
        dec+=(int(a[i])*(8**i))
    return dec

#Hexadecimal to decimal
def hex_to_decimal(a):
    a=list(a)
    dec=0
    a=a[::-1]
    C=['A','B','C','D','E','F']
    c=['a,','b','c','d','f']
    #converting octal to decimal
    for i in range(len(a)):
        if a[i] in C:
            a[i]=ord(a[i])-55
        elif a[i] in c:
            a[i]=ord(a[i])-87
    for i in range(len(a)):
        dec+=(int(a[i])*(16**i))
    return dec

#Octal to hexadecimal convertion
def octal_to_hex(a):
    return hexadec(octal_to_decimal(a))

#Hexadecimal to octal convertion
def hex_to_octal(a):
    return octal(hex_to_decimal(a))


#MATHS

def hex_add(a,b):
    print(a+"+"+b+" = "+hexadec(hex_to_decimal(a)+hex_to_decimal(b)))
def hex_sub(a,b):
    print(a+"-"+b+" = "+hexadec(hex_to_decimal(a)-hex_to_decimal(b)))
def oct_add(a,b):
    print(str(a)+"+"+str(b)+" = "+str(octal(octal_to_decimal(a)+octal_to_decimal(b))))
def oct_sub(a,b):
    print(str(a)+"-"+str(b)+" = "+str(octal(octal_to_decimal(a)-hex_to_decimal(b)))) 
    
hex_sub("974B","587C")
