#input_mahasiswa.py
"""Module untuk memasukkan data mahasiswa"""
def inputan():
    """Fungsi untuk memasukkan data mahasiswa"""
    mahasiswa = []

    try:
        total = int(input("\nMasukkan total mahasiswa: "))
        if total < 1:
            print("Total mahasiswa harus minimal 1.")
            return []
    except ValueError:
        print("Input tidak valid. Masukkan angka.")
        return []

    for i in range(total):
        input_mhs = input(f"\nMasukkan Nama Mahasiswa-{i+1}: ").strip()
        while not input_mhs:
            print("Nama tidak boleh kosong!")
            input_mhs = input(f"Masukkan Nama Mahasiswa-{i+1}: ").strip()

        input_npm = input(f"Masukkan NPM Mahasiswa-{i+1}: ").strip()
        while not input_npm:
            print("NPM tidak boleh kosong!")
            input_npm = input(f"Masukkan NPM Mahasiswa-{i+1}: ").strip()

        mahasiswa.append([input_npm, input_mhs])

    return mahasiswa
