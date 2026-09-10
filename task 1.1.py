import math

l = int(input())
r = int(input())
eps = 0.001
def f(x):
  return 0.1 * (x ** 2) - x * math.log(x)

if f(l) * f(r) < 0:
  while abs(l - r) > eps:
    b = l + (r-l) / 2
    if f(l) * f(b) < 0:
      r = b
    else:
      l = b
  print(r-l)
else:
  print('Корня не имеет')
