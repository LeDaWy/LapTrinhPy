import math

def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def dem_so_nguyen_to_nho_hon(n):
    dem = 0
    for i in range(2, n):
        if la_so_nguyen_to(i):
            dem += 1
    return dem

def cac_uoc_nguyen_to(n):
    danh_sach = []
    for i in range(2, n + 1):
        if n % i == 0 and la_so_nguyen_to(i):
            danh_sach.append(i)
    return danh_sach

n = int(input("Nhap n = "))

if la_so_nguyen_to(n):
    print(f"{n} la so nguyen to")
else:
    print(f"{n} khong phai la so nguyen to")

print(f"So luong so nguyen to < {n} la: {dem_so_nguyen_to_nho_hon(n)}")

print(f"Cac uoc cua {n} vua la uoc so vua la so nguyen to:")

for so in cac_uoc_nguyen_to(n):
    print(so, end=" ")