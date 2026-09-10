import math

l = int(input())
r = int(input())
eps = 0.001

def f(x):
  return 0.1 * (x ** 2) - x * math.log(x)

b = l - (f(l) * (r - l)) / (f(r) - f(l))
if f(l) * f(r) < 0:
  while abs(f(b)) > eps:
    if f(l) * f(b) < 0:
      r = b
    else:
      l = b
    b = l - (f(l) * (r - l)) / (f(r) - f(l))
  print(b)
else:
  print('Корней нет')
