def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
print("options")
print("1 add")
print("2 sub")
print("3 multiply")
print("4 divide")
print("press any other key for exit")
n1 = float(input("Enter a frist number "))
n2 = float(input("Enter a second number "))
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
            break
