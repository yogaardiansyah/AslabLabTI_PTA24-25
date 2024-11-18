#search_mahasiswa.py
"""Module untuk mencari data mahasiswa"""
def binary(mahasiswa):
    """Fungsi untuk mencari data mahasiswa dengan binary search"""
    if not mahasiswa:
        print("Data mahasiswa kosong. Input data terlebih dahulu.")
        return

    target_npm = input("Masukkan NPM untuk mencari: ").strip()

    mahasiswa = [[int(mhs[0]), mhs[1]] for mhs in mahasiswa]

    left, right = 0, len(mahasiswa) - 1
    while left <= right:
        mid = (left + right) // 2
        if mahasiswa[mid][0] == int(target_npm):
            print(f"\nMahasiswa ditemukan: NPM: {mahasiswa[mid][0]}, Nama: {mahasiswa[mid][1]}")
            return
        if mahasiswa[mid][0] < int(target_npm):
            left = mid + 1
        else:
            right = mid - 1

    print("Mahasiswa dengan NPM tersebut tidak ditemukan.")
