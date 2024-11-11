"""
Module seperti Receiptify
"""
def main():
    """
    Fungsi Main untuk mengakses program
    """
    try:
        total_order = int(input("Masukkan total order : "))
        npm_code = input("Masukkan NPM anda : ")
        mhs_name = input("Masukkan nama anda: ")

        with open("Receiptify.txt", "w", encoding="utf-8") as file:
            width = 87

            file.write(f"{' ' * ((width - len('Receiptify')) // 2)}Receiptify\n")
            file.write(f"{' ' * ((width - len('Last Month')) // 2)}Last Month\n\n")

            for order_num in range(1, total_order + 1):
                print(f"\n--- Order #{order_num:02d} ---")
                total_lagu = int(input(f"Masukkan total lagu untuk order ke {order_num} ini: "))
                total_durasi = 0

                file.write(f"Order #{order_num:02d}\n")
                file.write("Monday, 11 November 2024\n")
                file.write("=" * 87 + "\n")
                file.write("QTY\tItem" + " " * (69) + "AMT\n")
                file.write("=" * 87 + "\n")

                for x in range(1, total_lagu + 1):
                    jdl_lagu = input(f"Masukkan judul lagu ke-{x:02d}: ")
                    menit = int(input(f"Masukkan durasi menit untuk '{jdl_lagu}': "))
                    detik = int(input(f"Masukkan durasi detik untuk '{jdl_lagu}': "))
                    durasi_total_detik = menit * 60 + detik

                    file.write(f"{x:02d}\t{jdl_lagu}{' '*(72-len(jdl_lagu))}{menit}:{detik:02d}\n")
                    total_durasi += durasi_total_detik

                total_menit = total_durasi // 60
                total_detik = total_durasi % 60

                file.write("=" * 87 + "\n")
                file.write(f"Song Count\t:{' ' * (63)}{total_lagu}\n")
                file.write(f"Total\t\t:{' ' * (63)}{total_menit}:{total_detik:02d}\n")
                file.write("=" * 87 + "\n\n")

            file.write("Card # : PAP1PTA24\n")
            file.write(f"NPM Anda : {npm_code}\n")
            file.write(f"Nama Anda : {mhs_name}\n\n")
            file.write(f"{' ' * ((width - len('Thank you')) // 2)}Thank you\n")
            file.write(f"{' ' * ((width - len('for Using Program')) // 2)}for Using Program\n")

        print("Daftar lagu berhasil disimpan di Receiptify.txt")

    except ValueError:
        print("Input tidak valid, masukkan angka yang benar.")

if __name__ == "__main__":
    main()
