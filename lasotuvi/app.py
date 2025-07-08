# -*- coding: utf-8 -*-
"""
(c) 2016 doanguyen <dungnv2410@gmail.com>.
"""
from lasotuvi.AmDuong import (diaChi, dichCung, ngayThangNam,
                              ngayThangNamCanChi, nguHanh, nguHanhNapAm,
                              thienCan, timCoThan, timCuc, timHoaLinh,
                              timLuuTru, timPhaToai, timThienKhoi, timThienMa,
                              timThienQuanThienPhuc, timTrangSinh, timTriet,
                              timTuVi)
from lasotuvi.DiaBan import diaBan
from lasotuvi.Lich_HND import S2L
from lasotuvi.Sao import (saoAnQuang, saoBachHo, saoBacSy, saoBatToa, saoBenh,
                          saoBenhPhu, saoCoThan, saoCuMon, saoDaiHao, saoDaLa,
                          saoDaoHoa, saoDauQuan, saoDeVuong, saoDiaGiai,
                          saoDiaKhong, saoDiaKiep, saoDiaVong, saoDieuKhach,
                          saoDuong, saoDuongPhu, saoGiaiThan, saoHoaCai,
                          saoHoaKhoa, saoHoaKy, saoHoaLoc, saoHoaQuyen,
                          saoHoaTinh, saoHongLoan, saoHuuBat, saoHyThan,
                          saoKiepSat, saoKinhDuong, saoLamQuan, saoLiemTrinh,
                          saoLinhTinh, saoLocTon, saoLongDuc, saoLongTri,
                          saoLucSi, saoLuuHa, saoMo, saoMocDuc, saoNguyetDuc,
                          saoPhaQuan, saoPhaToai, saoPhiLiem, saoPhongCao,
                          saoPhucBinh, saoPhucDuc, saoPhuongCac, saoQuanDoi,
                          saoQuanPhu2, saoQuanPhu3, saoQuaTu, saoQuocAn,
                          saoSuy, saoTamThai, saoTangMon, saoTaPhu, saoTauThu,
                          saoThai, saoThaiAm, saoThaiDuong, saoThaiPhu,
                          saoThaiTue, saoThamLang, saoThanhLong, saoThatSat,
                          saoThienCo, saoThienDong, saoThienDuc, saoThienGiai,
                          saoThienHinh, saoThienHu, saoThienHy, saoThienKhoc,
                          saoThienKhoi, saoThienKhong, saoThienLa,
                          saoThienLuong, saoThienMa, saoThienPhu, saoThienPhuc,
                          saoThienQuan, saoThienQuy, saoThienRieu, saoThienSu,
                          saoThienTai, saoThienTho, saoThienThuong,
                          saoThienTru, saoThienTuong, saoThienViet, saoThienY,
                          saoThieuAm, saoThieuDuong, saoTieuHao, saoTrangSinh,
                          saoTrucPhu, saoTu, saoTuePha, saoTuongQuan, saoTuPhu,
                          saoTuVi, saoTuyet, saoVanKhuc, saoVanTinh,
                          saoVanXuong, saoVuKhuc)
from lasotuvi.ThienBan import lapThienBan


def lapDiaBan(diaBan: diaBan, nn, tt, nnnn, gioSinh, gioiTinh, duongLich, timeZone):
    if duongLich:
        print("[DEBUG] ngay duong:",nn, tt, nnnn)
        nn, tt, nnnn, thangNhuan = ngayThangNam(nn, tt, nnnn, duongLich, timeZone)
        print("[DEBUG]",nn, tt, nnnn, thangNhuan)
    canThang, canNam, chiNam = ngayThangNamCanChi(nn, tt, nnnn, False, timeZone)

    diaBan = diaBan(tt, gioSinh)

    amDuongNamSinh = thienCan[canNam]["amDuong"]
    amDuongChiNamSinh = diaChi[chiNam]["amDuong"]

    # Bản Mệnh chính là Ngũ hành nạp âm của năm sinh
    # banMenh = nguHanhNapAm(canNam, chiNam)

    hanhCuc = timCuc(diaBan.cungMenh, canNam)
    cuc = nguHanh(hanhCuc)
    cucSo = cuc["cuc"]

    # Nhập đại hạn khi đã biết được số cục
    # Theo sách Số tử vi dưới góc nhìn khoa học
    # Dương Nam - Âm Nữ theo chiều thuận
    # Âm Nam - Dương Nữ theo chiều nghịch
    diaBan = diaBan.nhapDaiHan(cucSo, gioiTinh * amDuongChiNamSinh)

    # Nhập tiểu hạn
    khoiHan = dichCung(11, -3 * (chiNam - 1))
    diaBan = diaBan.nhapTieuHan(khoiHan, gioiTinh, chiNam)

    # Bắt đầu an Tử vi tinh hệ
    viTriTuVi = timTuVi(cucSo, nn)
    diaBan.nhapSao(viTriTuVi, saoTuVi)

    viTriLiemTrinh = dichCung(viTriTuVi, 4)
    diaBan.nhapSao(viTriLiemTrinh, saoLiemTrinh)

    viTriThienDong = dichCung(viTriTuVi, 7)
    diaBan.nhapSao(viTriThienDong, saoThienDong)

    viTriVuKhuc = dichCung(viTriTuVi, 8)
    diaBan.nhapSao(viTriVuKhuc, saoVuKhuc)

    vitriThaiDuong = dichCung(viTriTuVi, 9)
    diaBan.nhapSao(vitriThaiDuong, saoThaiDuong)

    viTriThienCo = dichCung(viTriTuVi, 11)
    diaBan.nhapSao(viTriThienCo, saoThienCo)

    # Thiên phủ tinh hệ
    # viTriTuVi = 4
    viTriThienPhu = dichCung(3, 3 - viTriTuVi)
    diaBan.nhapSao(viTriThienPhu, saoThienPhu)

    viTriThaiAm = dichCung(viTriThienPhu, 1)
    diaBan.nhapSao(viTriThaiAm, saoThaiAm)

    viTriThamLang = dichCung(viTriThienPhu, 2)
    diaBan.nhapSao(viTriThamLang, saoThamLang)

    viTriCuMon = dichCung(viTriThienPhu, 3)
    diaBan.nhapSao(viTriCuMon, saoCuMon)

    viTriThienTuong = dichCung(viTriThienPhu, 4)
    diaBan.nhapSao(viTriThienTuong, saoThienTuong)

    viTriThienLuong = dichCung(viTriThienPhu, 5)
    diaBan.nhapSao(viTriThienLuong, saoThienLuong)

    viTriThatSat = dichCung(viTriThienPhu, 6)
    diaBan.nhapSao(viTriThatSat, saoThatSat)

    viTriPhaQuan = dichCung(viTriThienPhu, 10)
    diaBan.nhapSao(viTriPhaQuan, saoPhaQuan)

    # Vòng Lộc tồn
    # Vị trí sao Lộc tồn ở Can của năm sinh trên địa bàn
    #  sao Bác sỹ ở cùng cung với Lộc tồn
    viTriLocTon = thienCan[canNam]["vitriDiaBan"]
    diaBan.nhapSao(viTriLocTon, saoLocTon, saoBacSy)

    amDuongNamNu = gioiTinh * amDuongNamSinh
    viTriLucSi = dichCung(viTriLocTon, 1 * amDuongNamNu)
    diaBan.nhapSao(viTriLucSi, saoLucSi)

    viTriThanhLong = dichCung(viTriLocTon, 2 * amDuongNamNu)
    diaBan.nhapSao(viTriThanhLong, saoThanhLong)

    viTriTieuHao = dichCung(viTriLocTon, 3 * amDuongNamNu)
    diaBan.nhapSao(viTriTieuHao, saoTieuHao)

    viTriTuongQuan = dichCung(viTriLocTon, 4 * amDuongNamNu)
    diaBan.nhapSao(viTriTuongQuan, saoTuongQuan)

    viTriTauThu = dichCung(viTriLocTon, 5 * amDuongNamNu)
    diaBan.nhapSao(viTriTauThu, saoTauThu)

    viTriPhiLiem = dichCung(viTriLocTon, 6 * amDuongNamNu)
    diaBan.nhapSao(viTriPhiLiem, saoPhiLiem)

    viTriHyThan = dichCung(viTriLocTon, 7 * amDuongNamNu)
    diaBan.nhapSao(viTriHyThan, saoHyThan)

    viTriBenhPhu = dichCung(viTriLocTon, 8 * amDuongNamNu)
    diaBan.nhapSao(viTriBenhPhu, saoBenhPhu)

    viTriDaiHao = dichCung(viTriLocTon, 9 * amDuongNamNu)
    diaBan.nhapSao(viTriDaiHao, saoDaiHao)

    viTriPhucBinh = dichCung(viTriLocTon, 10 * amDuongNamNu)
    diaBan.nhapSao(viTriPhucBinh, saoPhucBinh)

    viTriQuanPhu2 = dichCung(viTriLocTon, 11 * amDuongNamNu)
    diaBan.nhapSao(viTriQuanPhu2, saoQuanPhu2)

    # Vòng Địa chi - Thái tuế
    viTriThaiTue = chiNam
    diaBan.nhapSao(viTriThaiTue, saoThaiTue)

    viTriThieuDuong = dichCung(viTriThaiTue, 1)
    diaBan.nhapSao(viTriThieuDuong, saoThieuDuong, saoThienKhong)

    viTriTangMon = dichCung(viTriThaiTue, 2)
    diaBan.nhapSao(viTriTangMon, saoTangMon)

    viTriThieuAm = dichCung(viTriThaiTue, 3)
    diaBan.nhapSao(viTriThieuAm, saoThieuAm)

    viTriQuanPhu3 = dichCung(viTriThaiTue, 4)
    diaBan.nhapSao(viTriQuanPhu3, saoQuanPhu3)

    viTriTuPhu = dichCung(viTriThaiTue, 5)
    diaBan.nhapSao(viTriTuPhu, saoTuPhu, saoNguyetDuc)

    viTriTuePha = dichCung(viTriThaiTue, 6)
    diaBan.nhapSao(viTriTuePha, saoTuePha)

    viTriLongDuc = dichCung(viTriThaiTue, 7)
    diaBan.nhapSao(viTriLongDuc, saoLongDuc)

    viTriBachHo = dichCung(viTriThaiTue, 8)
    diaBan.nhapSao(viTriBachHo, saoBachHo)

    viTriPhucDuc = dichCung(viTriThaiTue, 9)
    diaBan.nhapSao(viTriPhucDuc, saoPhucDuc, saoThienDuc)

    viTriDieuKhach = dichCung(viTriThaiTue, 10)
    diaBan.nhapSao(viTriDieuKhach, saoDieuKhach)

    viTriTrucPhu = dichCung(viTriThaiTue, 11)
    diaBan.nhapSao(viTriTrucPhu, saoTrucPhu)

    #  Vòng ngũ hành cục Tràng sinh
    # !!! Đã sửa !!! *LƯU Ý Phần này đã sửa* Theo cụ Thiên Lương: Nam -> Thuận,
    # Nữ -> Nghịch (Không phù hợp)
    # **ISSUE 2**: Dương nam, Âm nữ theo chiều thuận, Âm nam Dương nữ theo
    # chiều nghịch

    viTriTrangSinh = timTrangSinh(cucSo)
    diaBan.nhapSao(viTriTrangSinh, saoTrangSinh)

    viTriMocDuc = dichCung(viTriTrangSinh, amDuongNamNu * 1)
    diaBan.nhapSao(viTriMocDuc, saoMocDuc)

    viTriQuanDoi = dichCung(viTriTrangSinh, amDuongNamNu * 2)
    diaBan.nhapSao(viTriQuanDoi, saoQuanDoi)

    viTriLamQuan = dichCung(viTriTrangSinh, amDuongNamNu * 3)
    diaBan.nhapSao(viTriLamQuan, saoLamQuan)

    viTriDeVuong = dichCung(viTriTrangSinh, amDuongNamNu * 4)
    diaBan.nhapSao(viTriDeVuong, saoDeVuong)

    viTriSuy = dichCung(viTriTrangSinh, amDuongNamNu * 5)
    diaBan.nhapSao(viTriSuy, saoSuy)

    viTriBenh = dichCung(viTriTrangSinh, amDuongNamNu * 6)
    diaBan.nhapSao(viTriBenh, saoBenh)

    viTriTu = dichCung(viTriTrangSinh, amDuongNamNu * 7)
    diaBan.nhapSao(viTriTu, saoTu)

    viTriMo = dichCung(viTriTrangSinh, amDuongNamNu * 8)
    diaBan.nhapSao(viTriMo, saoMo)

    viTriTuyet = dichCung(viTriTrangSinh, amDuongNamNu * 9)
    diaBan.nhapSao(viTriTuyet, saoTuyet)

    viTriThai = dichCung(viTriTrangSinh, amDuongNamNu * (-1))
    diaBan.nhapSao(viTriThai, saoThai)

    viTriDuong = dichCung(viTriTrangSinh, amDuongNamNu * (-2))
    diaBan.nhapSao(viTriDuong, saoDuong)

    # An sao đôi
    #    Kình dương - Đà la
    viTriDaLa = dichCung(viTriLocTon, -1)
    diaBan.nhapSao(viTriDaLa, saoDaLa)

    viTriKinhDuong = dichCung(viTriLocTon, 1)
    diaBan.nhapSao(viTriKinhDuong, saoKinhDuong)

    #  Không - Kiếp
    # Khởi giờ Tý ở cung Hợi, đếm thuận đến giờ sinh được cung Địa kiếp
    viTriDiaKiep = dichCung(11, gioSinh)
    diaBan.nhapSao(viTriDiaKiep, saoDiaKiep)

    viTriDiaKhong = dichCung(12, 12 - viTriDiaKiep)
    diaBan.nhapSao(viTriDiaKhong, saoDiaKhong)

    # print("[DEBUG] timHoaLinh", chiNam, gioSinh, gioiTinh, amDuongNamSinh)
    viTriHoaTinh, viTriLinhTinh = timHoaLinh(chiNam, gioSinh, gioiTinh, amDuongNamSinh)
    diaBan.nhapSao(viTriHoaTinh, saoHoaTinh)
    diaBan.nhapSao(viTriLinhTinh, saoLinhTinh)

    viTriLongTri = dichCung(5, chiNam - 1)
    diaBan.nhapSao(viTriLongTri, saoLongTri)

    viTriPhuongCac = dichCung(2, 2 - viTriLongTri)
    diaBan.nhapSao(viTriPhuongCac, saoPhuongCac, saoGiaiThan)

    viTriTaPhu = dichCung(5, tt - 1)
    diaBan.nhapSao(viTriTaPhu, saoTaPhu)

    viTriHuuBat = dichCung(2, 2 - viTriTaPhu)
    diaBan.nhapSao(viTriHuuBat, saoHuuBat)

    viTriVanKhuc = dichCung(5, gioSinh - 1)
    diaBan.nhapSao(viTriVanKhuc, saoVanKhuc)

    viTriVanXuong = dichCung(2, 2 - viTriVanKhuc)
    diaBan.nhapSao(viTriVanXuong, saoVanXuong)

    viTriTamThai = dichCung(5, tt + nn - 2)
    diaBan.nhapSao(viTriTamThai, saoTamThai)

    viTriBatToa = dichCung(2, 2 - viTriTamThai)
    diaBan.nhapSao(viTriBatToa, saoBatToa)

    # ! Vị trí sao Ân Quang - Thiên Quý
    # ! Lấy cung thìn làm mồng 1 đếm thuận đến ngày sinh,
    # ! lui lại một cung để lấy đó làm giờ tý đếm thuận đến giờ sinh là
    #  Ân Quang
    # ! Thiên Quý đối với Ân Quang qua trục Sửu Mùi
    # @ viTriAnQuang = dichCung(5, nn + gioSinh - 3)
    # @ viTriThienQuy = dichCung(2, 2 - viTriAnQuang)
    # Phía trên là cách an Quang-Quý theo cụ Vu Thiên
    # Sau khi tìm hiểu thì Quang-Quý sẽ được an theo Xương-Khúc như sau:
    # Ân Quang − Xem Văn Xương ở cung nào, kể cung ấy là mồng một
    # bắt đầu đếm thoe chiều thuận đến ngày sinh, lùi lại một cung,
    # an Ân Quang.
    # Thiên Quý − Xem Văn Khúc ở cung nào, kể cung ấy là mồng một,
    # !!! bắt đầu đếm theo chiều nghịch đến ngày sinh, lùi lại một cung,
    # an Thiên Quý.!!!
    # ??? Thiên Quý ở đối cung của Ân Quang qua trục Sửu Mùi mới chính xác???

    viTriAnQuang = dichCung(viTriVanXuong, nn - 2)
    diaBan.nhapSao(viTriAnQuang, saoAnQuang)

    viTriThienQuy = dichCung(2, 2 - viTriAnQuang)
    diaBan.nhapSao(viTriThienQuy, saoThienQuy)

    viTriThienKhoi = timThienKhoi(canNam)
    diaBan.nhapSao(viTriThienKhoi, saoThienKhoi)

    viTriThienViet = dichCung(5, 5 - viTriThienKhoi)
    diaBan.nhapSao(viTriThienViet, saoThienViet)

    viTriThienHu = dichCung(7, chiNam - 1)
    diaBan.nhapSao(viTriThienHu, saoThienHu)

    viTriThienKhoc = dichCung(7, -chiNam + 1)
    diaBan.nhapSao(viTriThienKhoc, saoThienKhoc)

    viTriThienTai = dichCung(diaBan.cungMenh, chiNam - 1)
    diaBan.nhapSao(viTriThienTai, saoThienTai)

    viTriThienTho = dichCung(diaBan.cungThan, chiNam - 1)
    diaBan.nhapSao(viTriThienTho, saoThienTho)

    viTriHongLoan = dichCung(4, -chiNam + 1)
    diaBan.nhapSao(viTriHongLoan, saoHongLoan)

    viTriThienHy = dichCung(viTriHongLoan, 6)
    diaBan.nhapSao(viTriThienHy, saoThienHy)

    #  Thiên Quan - Thiên Phúc
    viTriThienQuan, viTriThienPhuc = timThienQuanThienPhuc(canNam)
    diaBan.nhapSao(viTriThienQuan, saoThienQuan)
    diaBan.nhapSao(viTriThienPhuc, saoThienPhuc)

    viTriThienHinh = dichCung(10, tt - 1)
    diaBan.nhapSao(viTriThienHinh, saoThienHinh)

    viTriThienRieu = dichCung(viTriThienHinh, 4)
    diaBan.nhapSao(viTriThienRieu, saoThienRieu, saoThienY)

    viTriCoThan = timCoThan(chiNam)
    diaBan.nhapSao(viTriCoThan, saoCoThan)

    viTriQuaTu = dichCung(viTriCoThan, -4)
    diaBan.nhapSao(viTriQuaTu, saoQuaTu)

    viTriVanTinh = dichCung(viTriKinhDuong, 2)
    diaBan.nhapSao(viTriVanTinh, saoVanTinh)

    viTriDuongPhu = dichCung(viTriVanTinh, 2)
    diaBan.nhapSao(viTriDuongPhu, saoDuongPhu)

    viTriQuocAn = dichCung(viTriDuongPhu, 3)
    diaBan.nhapSao(viTriQuocAn, saoQuocAn)

    # Thai phụ - Phong Cáo
    viTriThaiPhu = dichCung(viTriVanKhuc, 2)
    diaBan.nhapSao(viTriThaiPhu, saoThaiPhu)

    viTriPhongCao = dichCung(viTriVanKhuc, -2)
    diaBan.nhapSao(viTriPhongCao, saoPhongCao)

    # Thiên giải - Địa giải
    #    Theo cụ Thiên Lương: Lấy cung Thân làm tháng Giêng, đếm thuận nhưng
    #    nhảy cung là Thiên giải. Một số trang web đếm nhưng không nhảy cung???
    #    Liệu phương cách nào đúng?
    viTriThienGiai = dichCung(9, (2 * tt) - 2)
    diaBan.nhapSao(viTriThienGiai, saoThienGiai)

    viTriDiaGiai = dichCung(viTriTaPhu, 3)
    diaBan.nhapSao(viTriDiaGiai, saoDiaGiai)

    # Thiên la - Địa võng, Thiên thương - Thiên sứ
    viTriThienLa = 5
    diaBan.nhapSao(viTriThienLa, saoThienLa)

    viTriDiaVong = 11
    diaBan.nhapSao(viTriDiaVong, saoDiaVong)

    viTriThienThuong = diaBan.cungNoboc
    diaBan.nhapSao(viTriThienThuong, saoThienThuong)

    viTriThienSu = diaBan.cungTatAch
    diaBan.nhapSao(viTriThienSu, saoThienSu)

    # Vòng Thiên mã
    viTriThienMa = timThienMa(chiNam)
    diaBan.nhapSao(viTriThienMa, saoThienMa)

    viTriHoaCai = dichCung(viTriThienMa, 2)
    diaBan.nhapSao(viTriHoaCai, saoHoaCai)

    viTriKiepSat = dichCung(viTriThienMa, 3)
    diaBan.nhapSao(viTriKiepSat, saoKiepSat)

    viTriDaoHoa = dichCung(viTriKiepSat, 4)
    diaBan.nhapSao(viTriDaoHoa, saoDaoHoa)

    # Phá toái
    viTriPhaToai = timPhaToai(chiNam)
    diaBan.nhapSao(viTriPhaToai, saoPhaToai)

    # Đẩu quân
    viTriDauQuan = dichCung(chiNam, -tt + gioSinh)
    diaBan.nhapSao(viTriDauQuan, saoDauQuan)

    #  Tứ Hóa
    # An theo 10 câu của cụ Thiên Lương trong cuốn
    # Số tử vi dưới mắt khoa học

    if canNam == 1:
        viTriHoaLoc = viTriLiemTrinh
        viTriHoaQuyen = viTriPhaQuan
        viTriHoaKhoa = viTriVuKhuc
        viTriHoaKy = vitriThaiDuong
    elif canNam == 2:
        viTriHoaLoc = viTriThienCo
        viTriHoaQuyen = viTriThienLuong
        viTriHoaKhoa = viTriTuVi
        viTriHoaKy = viTriThaiAm
    elif canNam == 3:
        viTriHoaLoc = viTriThienDong
        viTriHoaQuyen = viTriThienCo
        viTriHoaKhoa = viTriVanXuong
        viTriHoaKy = viTriLiemTrinh
    elif canNam == 4:
        viTriHoaLoc = viTriThaiAm
        viTriHoaQuyen = viTriThienDong
        viTriHoaKhoa = viTriThienCo
        viTriHoaKy = viTriCuMon
    elif canNam == 5:
        viTriHoaLoc = viTriThamLang
        viTriHoaQuyen = viTriThaiAm
        viTriHoaKhoa = viTriHuuBat
        viTriHoaKy = viTriThienCo
    elif canNam == 6:
        viTriHoaLoc = viTriVuKhuc
        viTriHoaQuyen = viTriThamLang
        viTriHoaKhoa = viTriThienLuong
        viTriHoaKy = viTriVanKhuc
    elif canNam == 7:
        viTriHoaLoc = vitriThaiDuong
        viTriHoaQuyen = viTriVuKhuc
        viTriHoaKhoa = viTriThienDong
        viTriHoaKy = viTriThaiAm
    elif canNam == 8:
        viTriHoaLoc = viTriCuMon
        viTriHoaQuyen = vitriThaiDuong
        viTriHoaKhoa = viTriVanKhuc
        viTriHoaKy = viTriVanXuong
    elif canNam == 9:
        viTriHoaLoc = viTriThienLuong
        viTriHoaQuyen = viTriTuVi
        viTriHoaKhoa = viTriThienPhu
        viTriHoaKy = viTriVuKhuc
    elif canNam == 10:
        viTriHoaLoc = viTriPhaQuan
        viTriHoaQuyen = viTriCuMon
        viTriHoaKhoa = viTriThaiAm
        viTriHoaKy = viTriThamLang

    diaBan.nhapSao(viTriHoaLoc, saoHoaLoc)
    diaBan.nhapSao(viTriHoaQuyen, saoHoaQuyen)
    diaBan.nhapSao(viTriHoaKhoa, saoHoaKhoa)
    diaBan.nhapSao(viTriHoaKy, saoHoaKy)

    #  An Lưu Hà - Thiên Trù
    # Sách cụ Thiên Lương không đề cập đến 2 sao này
    # Mong mọi người kiểm chứng
    viTriLuuHa, viTriThienTru = timLuuTru(canNam)
    diaBan.nhapSao(viTriLuuHa, saoLuuHa)
    diaBan.nhapSao(viTriThienTru, saoThienTru)

    # An Tuần, Triệt
    ketThucTuan = dichCung(chiNam, 10 - canNam)
    viTriTuan1 = dichCung(ketThucTuan, 1)
    viTriTuan2 = dichCung(viTriTuan1, 1)
    diaBan.nhapTuan(viTriTuan1, viTriTuan2)

    viTriTriet1, viTriTriet2 = timTriet(canNam)
    diaBan.nhapTriet(viTriTriet1, viTriTriet2)
    return diaBan


def format_thien_ban(data):
    thien_ban = f"""
🔮 LÁ SỐ TỬ VI - THIÊN BÀN 🔮
───────────────────────────────
👤 Họ tên         : {data['ten']}
🧭 Giới tính      : {'Nam' if data['gioiTinh'] == 1 else 'Nữ'}
📆 Ngày dương     : {data['ngayDuong']:02d}/{data['thangDuong']:02d}/{data['namDuong']}
📅 Ngày âm        : {data['ngayAm']:02d}/{data['thangAm']:02d}/{data['namAm']} {'(Nhuận)' if data['thangNhuan'] else ''}
🌐 Múi giờ        : GMT+{data['timeZone']}
───────────────────────────────
🌟 Thiên can năm : {data['canNamTen']} ({data['canNam']})
🌀 Địa chi năm   : {data['chiNamTen']} ({data['chiNam']})
🌟 Thiên can tháng: {data['canThangTen']} ({data['canThang']})
🌀 Địa chi tháng : {data['chiThangTen']} ({data['chiThang']})
🌟 Thiên can ngày : {data['canNgayTen']} ({data['canNgay']})
🌀 Địa chi ngày  : {data['chiNgayTen']} ({data['chiNgay']})
───────────────────────────────
☯️ Âm dương năm sinh : {data['amDuongNamSinh']}
⚖️ Âm dương mệnh lý   : {data['amDuongMenh']}
⚙️ Cục số             : {data['tenCuc']} ({data['hanhCuc']})
🧿 Bản mệnh           : {data['banMenh']}
🌱 Sinh khắc          : {data['sinhKhac']}
🛡️ Mệnh chủ           : {data['menhChu']}
📚 Thân chủ           : {data['thanChu']}
───────────────────────────────
"""
    return thien_ban


def format_cung_data(cung_list):
    lines = []
    for cung in cung_list:
        lines.append("=" * 50)
        lines.append(
            f"Cung số {cung.cungSo} - {getattr(cung, 'cungTen', 'Không tên')} ({getattr(cung, 'cungChu', 'Chưa rõ')})"
        )
        lines.append(f"  - Hành cung     : {getattr(cung, 'hanhCung', 'Không rõ')}")

        am_duong_str = "Dương" if getattr(cung, "cungAmDuong", 0) == 1 else "Âm"
        lines.append(f"  - Âm Dương      : {am_duong_str}")
        lines.append(
            f"  - Cung Thân     : {'✅' if getattr(cung, 'cungThan', False) else '❌'}"
        )
        lines.append(f"  - Đại hạn       : {getattr(cung, 'cungDaiHan', 'Chưa rõ')}")
        lines.append(f"  - Tiểu hạn      : {getattr(cung, 'cungTieuHan', 'Chưa rõ')}")

        if getattr(cung, "trietLo", False):
            lines.append("  - Có Triệt Lộ ✂️")
        if getattr(cung, "tuanTrung", False):
            lines.append("  - Có Tuần Trung ⛓️")

        if getattr(cung, "cungSao", []):
            lines.append("  🌟 Danh sách sao:")
            for sao in cung.cungSao:
                ten = sao.get("saoTen", "?")
                hanh = sao.get("saoNguHanh", "?")
                loai = sao.get("saoLoai", "?")
                dac_tinh = sao.get("saoDacTinh", "")
                lines.append(
                    f"    - {ten} ({hanh}) [Loại {loai}]{' - ' + dac_tinh if dac_tinh else ''}"
                )
        else:
            lines.append("  🚫 Không có sao")

        lines.append("")  # Dòng trống giữa các cung

    return "\n".join(lines)


# diaban = lapDiaBan(
#     diaBan, nn=2, tt=1, nnnn=2023, gioSinh=3, gioiTinh=1, duongLich=1, timeZone=7
# )
# thienban = lapThienBan(nn=2, tt=1, nnnn=2023, gioSinh=3, gioiTinh=1, ten="asdf", diaBan=diaban)
# laso = {"thienBan": thienban, "thapNhiCung": diaban.thapNhiCung}
diaban = lapDiaBan(
    diaBan, nn=26, tt=10, nnnn=2002, gioSinh=3, gioiTinh=0, duongLich=1, timeZone=7
)
thienban = lapThienBan(nn=26, tt=10, nnnn=2002, gioSinh=3, gioiTinh=0, ten="asdf", diaBan=diaban)
laso = {"thienBan": thienban, "thapNhiCung": diaban.thapNhiCung}


# print(laso['thienBan'].__dict__)
print(format_thien_ban(laso['thienBan'].__dict__))

print(format_cung_data(laso['thapNhiCung']))
# for la in laso['thapNhiCung']:
#     print(la.__dict__)

# import requests
# from datetime import datetime
# from lasotuvi.prompt_template import make_prompt_luan_giai


# def chat_with_ollama(model="llama3.2:3b", log_file="log_luan_giai.txt"):
#     url = "http://localhost:11434/api/generate"
#     headers = {"Content-Type": "application/json"}

#     # Tạo prompt
#     prompt = make_prompt_luan_giai(
#         format_thien_ban(laso["thienBan"].__dict__),
#         format_cung_data(laso["thapNhiCung"])
#     )

#     data = {
#         "model": model,
#         "prompt": prompt,
#         "stream": False,
#     }

#     response = requests.post(url, headers=headers, json=data)

#     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#     if response.status_code == 200:
#         result_text = response.json().get("response", "")
#     else:
#         result_text = f"Lỗi: {response.status_code} - {response.text}"

#     # Ghi log
#     with open(log_file, "a", encoding="utf-8") as f:
#         f.write(f"\n================== {timestamp} ==================\n")
#         f.write("🔸 PROMPT:\n")
#         f.write(prompt.strip() + "\n\n")
#         f.write("🔸 RESPONSE:\n")
#         f.write(result_text.strip() + "\n")
#         f.write("=" * 60 + "\n")

#     return result_text


# # Ví dụ sử dụng
# if __name__ == "__main__":
#     reply = chat_with_ollama()
#     print("🧠 Bot trả lời:\n", reply)
