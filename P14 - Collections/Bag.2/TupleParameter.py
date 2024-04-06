# Di dalam python, kita dapat memberikan tanda * untuk menandakan sebuah parameter
# dapat menerima banyak argumen

def coba(*param):
    # parameter dengan tanda * akan menjadi tuple
    print(type(param))
    
    # kita dapat mengiterasi tuple tersebut selayaknya tuple biasa
    for x in param:
        print(x)
        
    # bisa juga menunggunakakn object list iterator
    li = iter(param)
    print()
    print(next(li))
    
# contoh implementasi functional programming
def sum(*values):
    if (len(values) == 1):
        return values[0]
    
    return values[0] + sum(*values[1:]) # kita dapat memberikan tanda * pada argumen untuk memecah list/tuple menjadi argumen terpisah
    # sum(*values) menjadi sum(values[0], values[1], values[3], ...)    
def main():
    # salah satu contoh dari penggunaan tanda * ada pada fungsi print()
    print(1,2,3,4,5) # parameter values ditandai dengan * sehingga dapat menerima lebih dari 1 argumen
    
    coba(10,20,30,40,50)
    
    # coba sum
    print(sum(1,2,3,4,5,6,7,8,9,10))
    
if __name__ == '__main__':
    main()      
        