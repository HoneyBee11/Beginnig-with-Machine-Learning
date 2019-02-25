#Program to perform basic Fuzzy Operations like Union, Intersection, Complement, Product

a = [0,0.2,0.35,0.65,0.85,1]
b = [0,0.35,0.40,0.8,0.95,1]

union = []
print("OR(Union)")
for i in range(len(a)):
    union.append(max(a[i],b[i]))
print(union)

intersection = []
print("\n\n""AND(Intersection)")
for i in range(len(a)):
    intersection.append(min(a[i],b[i]))
print(intersection)

complementA = []
complementB = []
print("\n\n""Complement")
for i in range(len(a)):
    complementA.append(round(1-a[i],2))
    complementB.append(round(1-b[i],2))
print("A's Complement")
print(complementA)
print("B's Complement")
print(complementB)

product = []
print("\n\n""Product")
for i in range(len(a)):
    product.append(round(a[i]*b[i],2))
print(product)

