# List dasar di python

def main():
    # Mendefinisikan & membuat list
    print("Mendefinisikan & membuat list:")
    list1 = []                  # list kosong
    print("list1: ", list1)
    list2 = [1,3,5,7]           # buat langsung diisi
    print("list2: ", list2)
    list3 = list()              # buat list dg konstuktor
    print("list3: ", list3 )
    list4 = list([2,4,6,8,10])
    print("list4: ", list4)
    
    # Indexing & slicing
    print("\nIndexing & slicing:")
    print("list4[0]: ", list4[0])
    print("list4[1:4]: ", list4[1:4])
    print("list4[:]: ", list4[:])
    print("list4[2:1]: ", list4[2:1])
    print("list4[2:]: ", list4[2:])
    print("list4[:3]: ", list4[:3])
    print("list4[-1]: ", list4[-1])
    print("list4[-2:]: ", list4[-2:])
    print("list4[:-2]: ", list4[:-2])
    print("list4[-3:-1]: ", list4[-3:-1])
    print("list4[-1:-3]: ", list4[-1:-3])
    
    print("\nList operations:")
    list5 = list2 + list4
    print("list5: ", list5)
    list5[8] = 14
    print("list5: ", list5)
    list5[4:7] = [9,11]
    print("list5: ", list5)
    print("len(list5): ", len(list5))
    list6 = [list2, list4]
    print("list6: ", list6)    
    
    del list5[6]
    print("list5: ", list5)
    del list5[4:6]
    print("list5: ", list5)
    del list5[3:]
    print("list5: ", list5)
    del list5[:]
    print("list5: ", list5)
    
    
if __name__ == "__main__":
    main()