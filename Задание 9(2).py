n = int(input())
prost = []
for i in range(2, n):
  count = 0
  for j in range(2, int(i ** 0.5) + 1):
    if i % j == 0:
      count += 1
      break
  if count == 0:
    prost.append(i)
print(prost)