import math

multi_table = [[0] * 10 for i in range(10)]


for i in range(1,10):
  for j in range(1,10):
    multi_table[i][j] = i * j

for i in range(1,10):
  for j in range(1,10):
    print(multi_table[i][j], end=", ")
  print()