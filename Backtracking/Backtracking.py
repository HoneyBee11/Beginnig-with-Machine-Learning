import math
x1=0
x2=1
v11 = 0.6
v21 = -0.1
v01 = 0.3
v12 = 0.4
v22 = -0.3
v02 = 0.5
w1 = 0.4
w2 = 0.1
w0 = -0.2
alpha = 0.25
zin1 = v01+(v11*x1)+(v21*x2)
zin2 = v02+(v12*x1)+(v22*x2)
z1 = 1/(1+math.exp(-zin1))
z2 = 1/(1+math.exp(-zin2))
yin = w0+(w1*z1)+(w2*z2)
y = 1/(1+math.exp(-yin))
fdyin = y*(1-y)
delta = (1-y)*fdyin
deltaw1 = alpha*delta*z1
deltaw2 = alpha*delta*z2
deltaw0 = alpha*delta
deltain1 = delta*w1
deltain2 = delta*w2
delta1 = deltain1*(z1*(1-z1))
delta2 = deltain2*(z2*(1-z2))
deltav11 = alpha*delta1*x1
deltav21 = alpha*delta1*x2
deltav01 = alpha*delta1
deltav12 = alpha*delta2*x1
deltav22 = alpha*delta2*x2
deltav02 = alpha*delta2
newv11 = v11+deltav11
newv12 = v12+deltav12
newv21 = v21+deltav21
newv22 = v22+deltav22
newv01 = v01+deltav01
newv02 = v02+deltav02
neww1 = w1+deltaw1
neww2 = w2+deltaw2
neww0 = w0+deltaw0
print("z1 : ",z1)
print("z2 : ",z2)
print("y : ",y)
print("new v11 : ",newv11)
print("new v12 : ",newv12)
print("new v21 : ",newv21)
print("new v22 : ",newv22)
print("new v01 : ",newv01)
print("new v02 : ",newv02)
print("new w1 : ",neww1)
print("new w2 : ",neww2)
print("new w0 : ",neww0)

