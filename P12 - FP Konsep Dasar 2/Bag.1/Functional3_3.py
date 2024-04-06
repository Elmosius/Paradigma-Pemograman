# Functional prefix notation

def foo(s):
    s1 = s + "foo"
    return s1

def bar(s):
    s2 = s + " bar"
    return s2

def yet_more(s):
    s3 = s + " yet more"
    return s3 

# Fungsi baru
def hello(s):
    s4 = s + " hello"
    return s4

def world(s):
    s5 = s + " world"
    return s5

def main():
    s = ""
    my = yet_more(bar(foo(s)))
    print("Functional prefix notation yet_more(bar(foo(s))):", my)

    # Menggunakan fungsi baru
    my_new = world(hello(s))
    print("Functional prefix notation world(hello(s)):", my_new)
    
if __name__ == "__main__":
    main()
