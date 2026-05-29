import math

la_so_chinh_phuong = lambda n: int(math.sqrt(n)) ** 2 == n

la_so_hoan_thien = lambda n: n > 1 and sum(i for i in range(1, n) if n % i == 0) == n

print("Cac so chinh phuong tu 1 den 10000:")

for so in range(1, 10001):
    if la_so_chinh_phuong(so):
        print(so, end=" ")

print("\n")

print("Cac so hoan thien tu 1 den 10000:")

for so in range(1, 10001):
    if la_so_hoan_thien(so):
        print(so, end=" ")