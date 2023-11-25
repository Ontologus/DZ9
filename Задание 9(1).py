def nod(a,b):
  while b:
    a, b = b, a % b
  return a
def nok(a,b):
  return a * b // nod(a,b)
a = int(input())
b = int(input())
print(nok(a, b))