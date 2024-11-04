cosplayer = ["borusushi", "xieduzizi", "xx_xning", "suiseiko", "senaka"]

def append_cos():
    print("Daftar cosplayer saat ini:", cosplayer)
    input_apnd = input("Masukkan nama cosplayer yang ingin ditambahkan: ")
    cosplayer.append(input_apnd)
    print(f'Cosplayer yang ditambahkan: {input_apnd}')
    print("Daftar cosplayer setelah ditambahkan:", cosplayer)

def insert_cos():
    print("Daftar cosplayer saat ini:", cosplayer)
    num_inserts = int(input("Berapa banyak cosplayer yang ingin dimasukan ke daftar? "))
    
    for i in range(num_inserts):
        position = int(input(f"Masukkan posisi cosplayer yang ingin dimasukan ke daftar {i + 1}: "))
        input_ins = input(f"Masukkan nama cosplayer {i + 1} yang ingin dimasukan ke daftar: ")
        cosplayer.insert(position, input_ins)
        print(f'Cosplayer yang dimasukan ke daftar: {input_ins} di posisi {position}')
    
    print("Daftar cosplayer setelah beberapa penyesuaian:", cosplayer)

def pop_cos():
    print("Daftar cosplayer saat ini:", cosplayer)
    if cosplayer:
        index = int(input("Masukkan indeks cosplayer yang ingin dihapus: "))
        if 0 <= index < len(cosplayer):
            popped = cosplayer.pop(index)
            print(f'Cosplayer yang dihapus: {popped}')
            print("Daftar cosplayer setelah pop:", cosplayer)
        else:
            print("Indeks tidak valid. Silakan masukkan indeks yang benar.")
    else:
        print("Daftar kosong, tidak ada yang dapat dihapus.")

def remove_cos():
    print("Daftar cosplayer saat ini:", cosplayer)
    input_rem = input("Masukkan nama cosplayer yang ingin dihapus: ")
    if input_rem in cosplayer:
        cosplayer.remove(input_rem)
        print(f'Cosplayer yang dihapus: {input_rem}')
        print("Daftar cosplayer setelah dihapus:", cosplayer)
    else:
        print(f"Cosplayer {input_rem} tidak ditemukan di daftar.")

def index_cos():
    print("Daftar cosplayer saat ini:", cosplayer)
    input_idx = input("Masukkan nama cosplayer untuk mencari indeksnya: ")
    if input_idx in cosplayer:
        idx = cosplayer.index(input_idx)
        print(f'Indeks dari cosplayer {input_idx}: {idx}')
    else:
        print(f"Cosplayer {input_idx} tidak ditemukan di daftar.")

def count_cos():
    print("Daftar cosplayer saat ini:", cosplayer)
    input_cnt = input("Masukkan nama cosplayer untuk menghitung jumlah kemunculannya: ")
    cnt = cosplayer.count(input_cnt)
    print(f'Cosplayer {input_cnt} muncul sebanyak {cnt} kali di daftar.')

def clear_cos():
    cosplayer.clear()
    print("Daftar cosplayer telah dikosongkan.")

def main():
    nama = "Yoga Ardianysah"
    kelas = "3IA25"
    npm = "51422643"
    print(f'Hallo, nama saya {nama}, dari kelas {kelas}, NPM {npm}')

    while True:
        print("""
============================================================================
        Selamat Datang di Menu Daftar Data Cosplayer
1. append Cosplayer              
2. insert Cosplayer
3. pop Cosplayer              
4. remove Cosplayer 
5. indeks Cosplayer
6. count Cosplayer
7. clear Cosplayer              
8. Exit                                     
============================================================================
    """)
        input_user = input("Masukkan pilihan menu (1-8): ")
        if input_user == '1':
            append_cos()
        elif input_user == '2':
            insert_cos()
        elif input_user == '3':
            pop_cos()
        elif input_user == '4':
            remove_cos()
        elif input_user == '5':
            index_cos()
        elif input_user == '6':
            count_cos()
        elif input_user == '7':
            clear_cos()
        elif input_user == '8':
            print("Keluar dari program.")
            break
        else:
            print("Input tidak valid. Silakan pilih menu dari 1 hingga 8.")

if __name__ == "__main__":
    main()
