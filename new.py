def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
print("option")
print("Add")
print("Sub")
print("Mul")
print("Div")
a1 = float(input("a1 "))
a2 = float(input("a2 "))
while 1:
    ch= input("Choice:")
    if ch in ('1','2','3','4'):
        if ch =='1':
            print(add(a1,a2));
        elif ch=='2':
            print(sub(a1,a2));
        elif ch=='3':
            print(mul(a1,a2));
        elif ch=='4':
            print(div(a1,a2));
            print();
        else:
            print("Error");