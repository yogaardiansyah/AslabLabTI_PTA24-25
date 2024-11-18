#main.py
"""Module sebagai main program"""
import input_mahasiswa as ipm  # import module
import sort_mahasiswa as sortm
import search_mahasiswa as srcm

def main():
    """Fungsi main untuk menjalankan program"""
    mahasiswa = []

    while True:
        print("""
          Menu Act6
        1. Input Data
        2. Sorting Data
        3. Searching Data
        4. Exit
        """)

        inputmenu = input("Masukkan pilihan menu: ").strip()

        if inputmenu == "1":
            mahasiswa = ipm.inputan()
            print("\nDaftar Mahasiswa:")
            for mhs in mahasiswa:
                print(f"NPM: {mhs[0]}, Nama: {mhs[1]}")
        elif inputmenu == "2":
            mahasiswa = sortm.seleksi(mahasiswa)
        elif inputmenu == "3":
            srcm.binary(mahasiswa)
        elif inputmenu == "4":
            print("Keluar dari program. Terima kasih!")
            break
        else:
            print("Menu tidak tersedia.")

if __name__ == "__main__":
    main()
