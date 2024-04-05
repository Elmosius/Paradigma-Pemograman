# TIpe data boolean
def main():
    # cek bilangan integer
    print("3 > 5 : ", 3 > 5)
    print("3 < 5 : ", 3 < 5)
    print("3 >= 5 : ", 3 >= 5)
    print("3 <= 5 : ", 3 <= 5)
    print("3 != 5 : ", 3 != 5)
    print("7 != 7 : ", 7 != 7)
    print("7 == 7 : ", 7 == 7)
    print()     # print baris kosong
    
    # cek bilangan pecahan
    print("3.4 > 5.7 : ", 3.4 > 5.7)
    print("3.4 < 5.7 : ", 3.4 < 5.7)
    print("3.4 >= 5.7 : ", 3.4 >= 5.7)
    print("3.4 <= 5.7 : ", 3.4 <= 5.7)
    print("3.4 != 5.7 : ", 3.4 != 5.7)
    print("7.5 != 7.5 : ", 7.5 != 7.5)
    print("7.5 == 7.5 : ", 7.5 == 7.5)
    print()     # print baris kosong
    
    # cek nilai boolean dari berbagai tipe data
    print("bool(5) : ", bool(5))                        # int
    print("bool(0) : ", bool(0))
    print("bool(15.3) : ", bool(15.3))                  # float
    print("bool(0.0) : ", bool(0.0))    
    print("bool('hallo') : ", bool('hallo'))            # str
    print("bool('') : ", bool(''))
    print("bool(3j) : ", bool(3j))                      # complex
    print("bool(0j) : ", bool(0j))
    print("bool(['satu', 'dua']) : ", bool(['satu', 'dua']))
    print("bool([]) : ", bool([]))
    print("bool(['satu', 'empat']) : ", bool(['satu', 'empat']))
    print("bool(()) : ", bool(()))
    print('bool({"nama" : "Daniel", "umur": "20"}) : ', 
          bool({"nama" : "Daniel", "umur": "20"}))
    print('bool({}) : ', bool({}))                      # dict
    print("bool(False) : ", bool(False))                # boolean
    print("bool(None) : ", bool(None))                  # None
    
    # Hampor semua nilai akan menghasilkan True jika ada isinya.
    # Semua string bernilai True, keculai string ksoong
    # Semua bilangan bernilai True kecuali 0
    # Semaa list, tuple, set, dict bernilai True, kecuali yang kosong
    
    obj_n = Kelas_length_bukan0()
    obj_0 = Kelas_length0()
    print("bool(obj_n) : ", bool(obj_n))
    print("bool(obj_0) : ", bool(obj_0))
    
    # Ovjek yg dibuat dari kelas yg fungsi __len__()-nya
    # me- return nilai 0 atau False maka bool()-nya False
    
class Kelas_length_bukan0():
    pass
    
class Kelas_length0():
    def __len__(self):
        return 0
    
if __name__ == "__main__":
    main()            