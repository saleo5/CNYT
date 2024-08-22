import math

def sumacomplejos(c1,c2):
    parteR = c1[0] + c2[0]
    parteI = c1[1] + c2[1]
    return parteR,parteI

def multiplicacion(c1,c2):
    p1 = c1[0] * c2[0] - c1[1] * c2[1]
    p2 = c2[0] * c1[1] + c2[1] * c1[0]
    return(p1,p2)

def resta(c1,c2):
    parteR = c1[0] - c2[0]
    parteI = c1[1] - c2[1]
    return parteR,parteI

def division(a,b):
    num1 = a[0] * b[0] - a[1] * b[1]
    num2 = a[1] * b[0] - a[1] * b[1]
    dem = b[0] ** 2 - b[1]
    return num1 / dem, num2 / dem

def modulo(c1):
    modu1 = ((c1[0] ** 2 + c1[1] ** 2) ** 0.5)
    return modu1

def conjugado(c1,c2):
    con1 = - c1[1]
    con2 = - c2[1]
    return (c1[0],con1),(c2[0],con2)

def polar(c1):
    r1 = modulo(c1)
    a = c1[0]
    b = c1[1]
    if a > 0 and b > 0:
        a1 = math.atan(b/a)
    elif a < 0 and b < 0:
        a1 = math.atan(b/a) + 180
    elif b > 0 and a < 0:
        a0 = math.atan(b/a) 
        a1 = 180 - a0
    elif b < 0 and a > 0:
        a0 = math.atan(b/a)
        a1 = 360 -a0
    return (r1,a1)

def cartesiano(c1):
    r,g = polar(c1)
    x = r * math.cos(g)
    y = r * math.sin(g)
    return(x,y)

def fase(c1):
    parteR = c1[0]
    parteI = c1[1]
    fase = math.atan2(parteI,parteR)
    return fase

if __name__ == '__main__':
    print(sumacomplejos((3,2),(-5,5.2)))
    print(resta((2,72),(15,55)))
    print(multiplicacion((2,12.1),(7,4)))
    print(division((12.2,45),(3,8)))
    print(modulo((15,6)))
    print(conjugado((7,-5),(-1,-1.5)))
    print(polar((7,5)))
    print(cartesiano((5,1)))
    print(fase((2,8)))