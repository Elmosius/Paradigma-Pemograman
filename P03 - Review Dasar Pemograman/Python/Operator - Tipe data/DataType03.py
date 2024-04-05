# Konversi tipe data

def main():
    a = 3
    b = 7.5
    c = 2j
     
    # konverso daro int ke float
    d = float(a)
     
    # konversi dari float ke int
    e = int(b)
     
    # konversi int ke complex
    f = complex(a)
     
    # konversi complex ke float (error karena tidak boleh)
    # g = float(c)
     
    print("d = ", d, ", tipe: ", type(d))
    print("e = ", e, ", tipe: ", type(e))
    print("f = ", f, ", tipe: ", type(f))
    
    h = c*c
    print("Bil complex x Bil complex: ", h)
    # j = float(h)      # TypeError: can't convert complex to float
    
if __name__ == "__main__":
    main()            