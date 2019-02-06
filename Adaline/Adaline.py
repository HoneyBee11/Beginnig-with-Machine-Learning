#Logical OR Function
#Bipolar bits

import numpy as np
x1 = np.array([1,1,-1,-1])
x2 = np.array([1,-1,1,-1])
t = np.array([1,1,1,-1])
alp=w1=w2=b=err=0.1
n=int(input("Enter number of epoch : "))
for i in range(n):
    print()
    print("*****Epoch ",i+1," begins*****")
    for j in range(len(x1)):
        if err==0:
            break
        yin = round((x1[j]*w1)+(x2[j]*w2)+b,2)
        w1=round(w1+(alp*(t[j]-yin)*x1[j]),2)
        w2=round(w2+(alp*(t[j]-yin)*x2[j]),2)
        b=round(b+alp*(t[j]-yin),2)
        err=round((t[j]-yin)*(t[j]-yin),2)
        print("yin : ",yin)
        print("w1 : ",w1)
        print("w2 : ",w2)
        print("b : ",b)
        print("error : ",err)
        print()
        
    print("*****Epoch ",i+1," ends*****")
    print()
    
print("Final yin : ",yin,"\n""Final w1 : ",w1,"\n""Final w2 : ",w2,"\n""Final b : ",b,"\n""Error : ",err)
