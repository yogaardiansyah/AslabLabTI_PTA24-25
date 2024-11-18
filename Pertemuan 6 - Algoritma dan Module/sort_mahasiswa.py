#sort_mahasiswa.py
"""Module untuk mensorting data mahasiswa"""
def seleksi(mahasiswa):
    """Fungsi untuk sorting data mahasiswa dengan selection sort"""
    if not mahasiswa:
        print("Data mahasiswa kosong. Input data terlebih dahulu.")
        return []

    for i, _ in enumerate(mahasiswa):
        min_index = i
        for j in range(i + 1, len(mahasiswa)):
            if int(mahasiswa[j][0]) < int(mahasiswa[min_index][0]):
                min_index = j

        mahasiswa[i], mahasiswa[min_index] = mahasiswa[min_index], mahasiswa[i]
        print(f"Iterasi {i+1}: {mahasiswa}")

    print("\nData mahasiswa berhasil diurutkan.")
    return mahasiswa
