chieu_dai = float(input("Nhap chieu dai day hinh khoi chu nhat (cm): "))
chieu_rong = float(input("Nhap chieu rong day hinh khoi chu nhat (cm): "))
chieu_cao = float(input("Nhap chieu cao hinh khoi chu nhat (cm): "))
so_luong_so_le = int(input("So luong so le can hien thi: "))

dien_tich_day = chieu_dai * chieu_rong
the_tich_hinh_khoi = dien_tich_day * chieu_cao

print(f"Dien tich day hinh chu nhat = {dien_tich_day:.2f} cm\u00b2")
print(f"The tich hinh khoi = {the_tich_hinh_khoi:.2f} cm\u00b3")