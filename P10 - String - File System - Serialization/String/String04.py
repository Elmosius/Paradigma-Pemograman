# Beberapa fungsi string tambahan
def main():
    bil1 = '123'
    bil2 = '45.67'
    bil3 = '45\u066067'
    bil4 = '127\u06600\u06600\u06601'
    print("isdigit", bil1, ":", bil1.isdigit())    
    print("isdigit", bil2, ":", bil2.isdigit())
    print("isdigit", bil3, ":", bil3.isdigit())
    print()
    print("isdecimal", bil1, ":", bil1.isdecimal())
    print("isdecimal", bil2, ":", bil2.isdecimal())
    print("isdecimal", bil3, ":", bil3.isdecimal())
    print("isdecimal", bil4, ":", bil4.isdecimal())
    print("isnumeric", bil1, ":", bil1.isnumeric())
    print("isnumeric", bil2, ":", bil2.isnumeric())
    print("isnumeric", bil3, ":", bil3.isnumeric())
    print()
    
    s1 = 'Hello World!'
    print("count", s1, ":", s1.count('l'))
    print("find", s1, ":", s1.find('l'))
    print("rfind", s1, ":", s1.rfind('1'))
    print("index", s1, ":", s1.index('o'))
    print("rindex", s1, ":", s1.rindex('o'))
    print("find", s1, ":", s1.find('m'))
    print()      
      
    # use a dictionary with ascii codes to replace
    # 83(S) with 80(P), 108(l) -> 109(m)
    mydict = {83:80, 108:109}
    txt = "Hello Sam! apa kabar?"
    print(txt, "->", txt.translate(mydict))
    print("split ' ':", txt.split(" "))
    print("split 'a':", txt.split("a"))
    print()
    txt2 = txt.split(" ")
    print("split ' ' join '_':", "_".join(txt2))
    print("replace a->A:", txt.replace('a', 'A'))
    
if __name__ == "__main__":
    main()