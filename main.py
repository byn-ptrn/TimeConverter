def main():
    # Welcome message
    print("=== TIME CONVERTER ===")
    print("Tekan Enter untuk memulai...")
    input()

    konversi_waktu()


def konversi_waktu():
    # Daftar satuan waktu yang valid
    satuan_valid = ['detik', 'menit', 'jam']

    # Input satuan waktu awal
    while True:
        satuan_awal = input("Masukkan satuan waktu awal (detik/menit/jam): ").lower()
        if satuan_awal in satuan_valid:
            break
        print("Satuan waktu tidak valid. Silakan coba lagi.")

    # Input jumlah waktu
    while True:
        try:
            jumlah = float(input("Masukkan jumlah waktu: "))
            break
        except ValueError:
            print("Masukan harus berupa angka. Silakan coba lagi.")

    # Input satuan waktu akhir
    while True:
        satuan_akhir = input("Masukkan satuan waktu akhir (detik/menit/jam): ").lower()
        if satuan_akhir in satuan_valid:
            break
        print("Satuan waktu tidak valid. Silakan coba lagi.")

    # Konversi ke detik
    if satuan_awal == 'menit':
        detik = jumlah * 60
    elif satuan_awal == 'jam':
        detik = jumlah * 3600
    else:
        detik = jumlah

    # Konversi dari detik ke satuan akhir
    if satuan_akhir == 'menit':
        hasil = detik / 60
    elif satuan_akhir == 'jam':
        hasil = detik / 3600
    else:
        hasil = detik

    # Tampilkan hasil
    print(f"{jumlah} {satuan_awal} = {hasil} {satuan_akhir}")


# Jalankan fungsi
if __name__ == "__main__":
    main()