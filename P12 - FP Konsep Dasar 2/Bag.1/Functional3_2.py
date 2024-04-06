# Object Oriented suffix notation

class MyClass:
    def __init__(self) -> None:
        self.s: str = ""
        
    def foo(self):
        self.s = self.s + "foo"
        return self
    
    def bar(self):
        self.s = self.s + " bar"
        return self
    
    def yet_more(self):
        self.s = self.s + " yet more"
        return self

    # Metode baru
    def hello(self):
        self.s = self.s + " hello"
        return self

    def world(self):
        self.s = self.s + " world"
        return self

def main():
    my = MyClass()
    my.foo().bar().yet_more()
    print("OOP suffix notation obj.foo().bar().yet_more()", my.s)

    # Menggunakan metode baru
    my.hello().world()
    print("OOP suffix notation obj.hello().world()", my.s)
    
if __name__ == "__main__":
    main()
