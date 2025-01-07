# Class untuk mengelola data mahasiswa
class Data:
    def __init__(self):
        self.mahasiswa = []

    def tambah_data(self, nama, nim, jurusan):
        self.mahasiswa.append({"Nama": nama, "NIM": nim, "Jurusan": jurusan})

    def get_data(self):
        return self.mahasiswa


# Class untuk menampilkan data dalam format tabel
class View:
    @staticmethod
    def tampilkan_data(data):
        if not data:
            print("Tidak ada data mahasiswa.")
            return
        
        print("=" * 40)
        print(f"{'Nama':<15} {'NIM':<10} {'Jurusan':<15}")
        print("=" * 40)
        for mhs in data:
            print(f"{mhs['Nama']:<15} {mhs['NIM']:<10} {mhs['Jurusan']:<15}")
        print("=" * 40)


# Class untuk memproses input dan validasi
class Process:
    @staticmethod
    def input_data():
        try:
            nama = input("Masukkan Nama: ").strip()
            if not nama:
                raise ValueError("Nama tidak boleh kosong.")
            
            nim = input("Masukkan NIM: ").strip()
            if not nim.isdigit():
                raise ValueError("NIM harus berupa angka.")
            
            jurusan = input("Masukkan Jurusan: ").strip()
            if not jurusan:
                raise ValueError("Jurusan tidak boleh kosong.")
            
            return nama, nim, jurusan
        except ValueError as e:
            print(f"Error: {e}")
            return None


# Main Program
def main():
    data = Data()
    view = View()
    
    while True:
        print("\n=== Menu ===")
        print("1. Tambah Data Mahasiswa")
        print("2. Tampilkan Data Mahasiswa")
        print("3. Keluar")
        pilihan = input("Pilih menu: ").strip()
        
        if pilihan == "1":
            hasil_input = Process.input_data()
            if hasil_input:
                nama, nim, jurusan = hasil_input
                data.tambah_data(nama, nim, jurusan)
                print("Data berhasil ditambahkan!")
        elif pilihan == "2":
            view.tampilkan_data(data.get_data())
        elif pilihan == "3":
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")


if __name__ == "__main__":
    main()