#Logical OR function
#Binary bits

import numpy as np
x1 = np.array([1,1,0,0])
x2 = np.array([1,0,1,0])
t = np.array([1,1,1,-1])
w1=w2=b=0
alp=1
th=0.2
n=int(input("Enter numbers of Epoch : "))
for i in range(n):
    print("*****Epcoh ",i+1," begins*****")
    for j in range(len(x1)):
        yin = b+(x1[j]*w1)+(x2[j]*w2)
        if yin>0.2:
            y=1
        else:
            y=0
        if y!=t[j]:
            w1=w1+(alp*t[j]*x1[j])
            w2=w2+(alp*t[j]*x2[j])
            b=b+(alp*t[j])
        print("yin : ",yin)
        print("y : ",y)
        print("w1 : ",w1)
        print("w2 : ",w2)
        print("b : ",b)
        print()
    print("*****Epcoh ", i + 1, " ends*****\n")
print("Final yin : ", yin)
print("Final y : ", y)
print("Final w1 : ", w1)
print("Final w2 : ", w2)
print("Final b : ", b)