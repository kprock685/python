def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
print("option 1,2,3,4")
n1 = float(input("n1 "))
n2 = float(input("n2 "))
while 1:
    ch= input("Choice:")
    if ch in ('1','2','3','4'):
        if ch =='1':
            print(add(n1,n2));
        elif ch=='2':
            print(sub(n1,n2));
        elif ch=='3':
            print(mul(n1,n2));
        elif ch=='4':
            print(div(n1,n2));
        else:
            print("Error");
