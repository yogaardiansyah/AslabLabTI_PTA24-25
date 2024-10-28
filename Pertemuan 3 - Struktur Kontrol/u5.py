def tampilkan_menu_utama():
    print("""
=======================================
    Selamat datang di Toko Baju
    1. Beli Baju
    2. Cek Stok Baju
    3. Hitung Total Pembelian
    4. Keluar dari Program
======================================  
    """)

def beli_baju(stok_cospa, stok_gildan, stok_printstar):
    print("\nMenu Beli Baju:")
    print("1. Baju Cospa - Rp500.000")
    print("2. Baju Gildan - Rp270.000")
    print("3. Baju Printstar - Rp100.000")
    
    pilihan = input("Pilih baju yang ingin dibeli (1-3): ")

    if pilihan == '1':
        harga = 500000
        jenis = 'Cospa'
        if stok_cospa <= 0:
            print("Stok Baju Cospa habis.")
            return 0, stok_cospa, stok_gildan, stok_printstar
    elif pilihan == '2':
        harga = 270000
        jenis = 'Gildan'
        if stok_gildan <= 0:
            print("Stok Baju Gildan habis.")
            return 0, stok_cospa, stok_gildan, stok_printstar
    elif pilihan == '3':
        harga = 100000
        jenis = 'Printstar'
        if stok_printstar <= 0:
            print("Stok Baju Printstar habis.")
            return 0, stok_cospa, stok_gildan, stok_printstar
    else:
        print("Pilihan tidak valid.")
        return 0, stok_cospa, stok_gildan, stok_printstar

    jumlah = input("Masukkan jumlah baju yang ingin dibeli: ")

    while True:
            jumlah = int(jumlah)
            if jumlah >= 1:
                if (pilihan == '1' and jumlah > stok_cospa) or \
                   (pilihan == '2' and jumlah > stok_gildan) or \
                   (pilihan == '3' and jumlah > stok_printstar):
                    print("Belanja kamu melebihi stok yang ada.")
                    return 0, stok_cospa, stok_gildan, stok_printstar
                else:
                    if pilihan == '1':
                        stok_cospa -= jumlah
                    elif pilihan == '2':
                        stok_gildan -= jumlah
                    elif pilihan == '3':    
                        stok_printstar -= jumlah

                    total_harga = harga * jumlah
                    print(f"Total harga untuk {jumlah} baju {jenis}: Rp{total_harga}")
                    return total_harga, stok_cospa, stok_gildan, stok_printstar
            else:
                print("Jumlah harus lebih dari 0.")
                return 0, stok_cospa, stok_gildan, stok_printstar
            
def cek_stok_baju(stok_cospa, stok_gildan, stok_printstar):
    print("\nStok Baju Tersedia:")
    print(f"Baju Cospa - Rp500.000 (Stok: {stok_cospa})")
    print(f"Baju Gildan - Rp270.000 (Stok: {stok_gildan})")
    print(f"Baju Printstar - Rp100.000 (Stok: {stok_printstar})")

def main():
    stok_cospa = 10
    stok_gildan = 10
    stok_printstar = 10
    total_pembelian = 0
    
    while True:
        tampilkan_menu_utama()
        pilihan = input("Masukkan pilihan menu: ")

        if pilihan == '1':
            harga, stok_cospa, stok_gildan, stok_printstar = beli_baju(stok_cospa, stok_gildan, stok_printstar)
            total_pembelian += harga
        elif pilihan == '2':
            cek_stok_baju(stok_cospa, stok_gildan, stok_printstar)
        elif pilihan == '3':
            print(f"Total Pembelian Anda: Rp{total_pembelian}")
        elif pilihan == '4':
            print("Terima kasih telah menggunakan program ini!")
            break
        else:
            print("Input salah, coba lagi.")
            continue

if __name__ == "__main__":
    main()
