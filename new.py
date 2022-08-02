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
a1 = int(input("Enter a first num "))
a2 = int(input("Enter a second num ")) 

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
    else:
        break
 # python programming
