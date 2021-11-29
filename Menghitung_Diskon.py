# IRSAN ACHMAD MAULIDAN S1/TI/01/A/P 43A87006210144
# PROGRAM MENGHITUNG HARGA DISKON GANDA

print("====SELAMAT DATANG DI TOKO KAMI====")
print("")
JumlahBarang = int(input("Masukan Jumlah Barang Anda = "))
HargaSatuan = int(input("Masukan Harga Satuan = Rp "))
HargaBarang = JumlahBarang*HargaSatuan
if (HargaBarang > 1500000):
    diskon1 = 35/100*HargaBarang
    diskon2 = (HargaBarang-diskon1)*15/100
    Potongan = diskon1+diskon2
elif (HargaBarang >= 750000 <= 1500000):
    diskon_1 = 15/100*HargaBarang
    diskon_2 = (HargaBarang-diskon_1)*10/100
    Potongan = diskon_1+diskon_2
else:
    Potongan = 0
HargaBayar = HargaBarang-Potongan
total = f"Total Harga Barang Anda = Rp  {HargaBarang:,}"
print(total)
total_diskon = f"Potongan Harga = Rp  {Potongan:,}"
print(total_diskon)
total_bayar = f"Harga yang Harus Anda Bayar = Rp  {HargaBayar:,}"
print(total_bayar)
print("")
print("====TERIMAKASIH SUDAH BERBELANJA====")
