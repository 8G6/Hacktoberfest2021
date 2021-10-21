sum    = lambda a,b             : a+(b/2)  
mul    = lambda h,fun,x,y,z     : h*fun(x,y,z) #y = mx + c; m = derivative, x=x value, c=step size

k_val  = lambda k               : (k[0]+(2*k[1])+(2*k[2])+k[3])/6 # k = (k1+2(k2)+2(k3)+k4)/6
eval   = lambda fun,x,h,y,k,z,l : fun(sum(x,h),sum(y,k),sum(z,l))

fun    = lambda x,y,z           : ((z**2)*x)-(y**2)  # reduced 1st order function 

h=0.2                            #step size
x0,y0,z0=0,1,0                   # x(0)=0, y(0)=1, y'(0)=0 or z(0)=0

k1=h*z0                          #f(x,y,z) = z , k1 = h*f(x,y,z) = h*z
l1=mul(h,fun,x0,y0,z0)           #l1 = h*g(x,y,z) 

k2=h*sum(z0,l1)                  #f(x,y,z) = z 
l2=h*eval(fun,x0,h,y0,k1,z0,l1)  #l2 = h*g(x+h/2,y+k/2,z+l/2)

k3=h*sum(z0,l2)                  #f(x,y,z) = z
l3=h*eval(fun,x0,h,y0,k2,z0,l2)  #l2 = h*g(x+h/2,y+k/2,z+l/2)

k4=h*(z0+l3)                     #f(x,y,z) = z , k4 = h*f(x+h,y+k3,z+l3) , k4 = h*(z+l3)

print(f"k1={k1}\nl1={l1}\nk2={k2}\nl2={l2}\nk3={k3}\nl3={l3}\nk4={k4}\n")
k=k_val([k1,k2,k3,k4])
print(f"y({h})={y0+k}")



