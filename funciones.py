
a,b = 0,1

while a<10:
    print(a)
    a,b = b,a+b
    
    
def sumar(a,b):
    c = a+b
    return c
print(sumar(3,8))

def sumarTres(a):
    x=a+3
    return x
y=sumarTres(7)+2
print(y)


x=int(input())
y= int(input())
z=x+y
print(z)

'''
funcion1()

x=int(input())
y= int(input())
return x+y
'''


def sumar(a,b):
    return a+b