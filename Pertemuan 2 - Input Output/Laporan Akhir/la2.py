def input_bangun_datar():
    panjang = int(input("Masukkan nilai panjang: "))
    lebar = int(input("Masukkan nilai lebar: "))
    tinggi = int(input("Masukkan nilai tinggi: "))
    alas = int(input("Masukkan nilai alas: "))
    jari_jari = int(input("Masukkan nilai jari-jari: "))
    sisi = int(input("Masukkan nilai sisi: "))
    diagonal1 = int(input("Masukkan nilai diagonal1: "))
    diagonal2 = int(input("Masukkan nilai diagonal2: "))
    sisi_miring = int(input("Masukkan nilai sisi miring: "))

    return panjang, lebar, tinggi, alas, jari_jari, sisi, diagonal1, diagonal2, sisi_miring

def hitung_bangunan(panjang,lebar,tinggi,alas,jari_jari,sisi,diagonal1,diagonal2,sisi_miring):

    def hitung_persegi(sisi):
        return sisi * sisi

    def hitung_persegi_panjang(panjang, lebar):
        return panjang * lebar

    def hitung_segitiga(alas, tinggi):
        return 0.5 * alas * tinggi

    def hitung_lingkaran(jari_jari):
        return 3.14 * jari_jari * jari_jari

    def hitung_layang_layang(diagonal1, diagonal2):
        return 0.5 * diagonal1 * diagonal2

    def hitung_trapesium(alas, sisi_miring, tinggi):
        return 0.5 * (alas + sisi_miring) * tinggi

    def hitung_jajar_genjang(alas, tinggi):
        return alas * tinggi

    def hitung_belah_ketupat(diagonal1, diagonal2):
        return 0.5 * diagonal1 * diagonal2

    tampilkan_hasil("Luas Persegi", hitung_persegi(sisi))
    tampilkan_hasil("Luas Persegi Panjang", hitung_persegi_panjang(panjang, lebar))
    tampilkan_hasil("Luas Segitiga", hitung_segitiga(alas, tinggi))
    tampilkan_hasil("Luas Lingkaran", hitung_lingkaran(jari_jari))
    tampilkan_hasil("Luas Layang-Layang", hitung_layang_layang(diagonal1, diagonal2))
    tampilkan_hasil("Luas Trapesium", hitung_trapesium(alas, sisi_miring, tinggi))
    tampilkan_hasil("Luas Jajar Genjang", hitung_jajar_genjang(alas, tinggi))
    tampilkan_hasil("Luas Belah Ketupat", hitung_belah_ketupat(diagonal1, diagonal2))

def tampilkan_hasil(nama_bangun, luas):
    print(f"{nama_bangun}: {luas}")

def main():
    print("=========================================")
    # print() print nama kalian, npm kalian, kelas kalian, pertemuan 2 dengan materi input output
    panjang,lebar,tinggi,alas,jari_jari,sisi,diagonal1,diagonal2,sisi_miring = input_bangun_datar()
    print("=========================================")
    hitung_bangunan(panjang,lebar,tinggi,alas,jari_jari,sisi,diagonal1,diagonal2,sisi_miring)
    print("=========================================")

if __name__ == '__main__':
    main()
