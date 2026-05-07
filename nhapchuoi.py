from collections import Counter

# Nhập 2 chuỗi
S1 = input("Nhập chuỗi S1: ")
S2 = input("Nhập chuỗi S2: ")

# Chuyển thành Counter
dict1 = Counter(S1)
dict2 = Counter(S2)

# =========================
# a) Ký tự xuất hiện trong cả 2 chuỗi
# =========================
common = dict1 & dict2

print("\na) Các ký tự xuất hiện trong cả 2 chuỗi:")
print(list(common.keys()))

# =========================
# b) Đếm ký tự khác nhau
# =========================
only_S1 = [char for char in dict1 if char not in dict2]
only_S2 = [char for char in dict2 if char not in dict1]

count_diff = len(only_S1) + len(only_S2)

print("\nb) Số ký tự khác nhau giữa 2 chuỗi:")
print(count_diff)

# =========================
# c) In các ký tự riêng của từng chuỗi
# =========================
print("\nc) Ký tự có trong S1 nhưng không có trong S2:")
print(only_S1)

print("\nKý tự có trong S2 nhưng không có trong S1:")
print(only_S2)