import math

# a) Giá trị tuyệt đối
abs_val = lambda n: abs(n)

# b) n + 15
plus_15 = lambda n: n + 15

# c) Tích x * y
multiply = lambda x, y: x * y

# d) Kiểm tra bội số của 13 hoặc 19
is_multiple_13_19 = lambda n: n % 13 == 0 or n % 19 == 0

# e) Diện tích hình tròn
area_circle = lambda r: math.pi * r * r

# f) Chu vi hình chữ nhật
perimeter_rect = lambda d, r: 2 * (d + r)

# g) Kiểm tra số chính phương
is_perfect_square = lambda n: int(math.sqrt(n))**2 == n

# h) Kiểm tra số nguyên tố
is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1))

# i) Kiểm tra tam giác và loại tam giác
triangle_type = lambda a, b, c: (
    "Không phải tam giác"
    if a + b <= c or a + c <= b or b + c <= a
    else "Tam giác đều"
    if a == b == c
    else "Tam giác cân"
    if a == b or b == c or a == c
    else "Tam giác vuông"
    if a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a
    else "Tam giác thường"
)



print("a)", abs_val(-5))
print("b)", plus_15(10))
print("c)", multiply(3, 4))
print("d)", is_multiple_13_19(26))
print("e)", area_circle(2))
print("f)", perimeter_rect(5, 3))
print("g)", is_perfect_square(16))
print("h)", is_prime(7))
print("i)", triangle_type(3, 4, 5))