
k_val  = lambda k   : (k[0]+(2*k[1])+(2*k[2])+K[3])/6

Fun    = lambda x,y : x+(y**0.5)

h,x,y=0.1,0,1


k_list = [
         lambda fun,x,y,h,T  : h*fun(x,y)*(T/T),
         lambda fun,x,y,h,K1 : h*fun((x+(h/2)),(y+(K1/2))),
         lambda fun,x,y,h,K2 : h*fun((x+(h/2)),(y+(K2/2))),
         lambda fun,x,y,h,K3 : h*fun(x+h,y+K3)
         ]

p=1

K=[]
u=[]
itrations = 10000
for i in range(itrations):
    for k in k_list:
        p=k(Fun,x,y,h,p)
        K.append(p)
    k=k_val(K)
    
    K=[]

    x+=h
    y+=k
    
    u.append([x,y])

for i in u:
    for j in i:
        print(j,end=' ')
    print()


