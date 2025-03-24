import math
x = 2
y = 2

print("Площадь окружности радиусом",dict(map(lambda x,y: (x, y),  [x],[math.pi*(y**2)])))

x = 10
y = 13
s = dict(map(lambda x,y: (x, y),  [(x,y)],[x*y]))
print("площадь прямоугольника размером",x,"x",y,":", s[(x,y)] )

a = 7
b = 5
h = 3
t = dict(map(lambda x: (x, (x[0]+x[1])/2*x[2]), [(a,b,h)]))
print("Площадь трапеции для a =",a, "b =",b,"h=",h, t[(a,b,h)])
