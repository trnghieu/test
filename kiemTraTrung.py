def kiemTraTrung(maSoSV):
    phanTuTrung = set()
    phanTuDaXet = set()

    for ma_so in maSoSV:
        if maSo in phanTuDaXet:
            phanTuTrung.add(maSo)
        else:
            phanTuDaXet.add(maSo)

    if phanTuTrung:
        print("Cac phan tu bi trung:", ", ".join(phanTuTrung))
    else:
        print("Khong co phan tu bi trung.")


# Ví dụ với danh sách mã số sinh viên
danhSachMaSo = ["16110001", "16110002", "16110001"]
kiemTraTrung(danhSachMaSo)