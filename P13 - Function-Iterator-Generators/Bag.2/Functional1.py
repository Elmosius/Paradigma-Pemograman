# Dalam functional programming, kita harus meminimalisir penggunaan statefull objects (salah satu contohnya File I/O).
# Namun jika memang dibutuhkan, kita dapat membungkus blok kode statfull ke dalam context manager di Python

def tulisFile(namaFile: str, isi: str):
    # Context manager menggunakan kata kunci "with"
    with open(namaFile, 'w') as f:
        f.write(isi)
    
    # Dengan context manager, kita tidak perlu menggunakan fungsi close() (sudah otomatis diclose oleh context managernya)
    
# Contoh fungsi yang tidak menggunakan state manager
def tulisFile(namaFile: str, isi: str):
    f = open(namaFile, 'w')
    f.write(isi)
    f.close()   # karena tidak pakai context manager, maka kita harus panggil method close() pada file agar tidak terjadi 
                # Resource leak
                          
def main():
    tulisFile("text.txt", "Hello World!")
    tulisFile("test2.txt", "Hello World 2!")

if __name__ == "__main__":
    main()