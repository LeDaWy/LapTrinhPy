import math

kiem_tra_so_chinh_phuong = lambda n: int(math.sqrt(n)) ** 2 == n

phan_loai_tam_giac = lambda a, b, c: (
    "Khong phai tam giac"
    if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a
    else "Tam giac deu"
    if a == b == c
    else "Tam giac vuong can"
    if (a == b or b == c or a == c) and
       (a * a + b * b == c * c or
        a * a + c * c == b * b or
        b * b + c * c == a * a)
    else "Tam giac can"
    if a == b or b == c or a == c
    else "Tam giac vuong"
    if a * a + b * b == c * c or
       a * a + c * c == b * b or
       b * b + c * c == a * a
    else "Tam giac thuong"
)

n = int(input("Nhap n: "))

if kiem_tra_so_chinh_phuong(n):
    print(f"{n} la so chinh phuong")
else:
    print(f"{n} khong phai la so chinh phuong")

a = int(input("Nhap canh a: "))
b = int(input("Nhap canh b: "))
c = int(input("Nhap canh c: "))

print(phan_loai_tam_giac(a, b, c))