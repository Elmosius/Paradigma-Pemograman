# Format string
import datetime

class Notification:
    def __init__(self, from_addr:str, to_addr:str, 
                subject:str, message:str):
        
        self.from_addr = from_addr
        self.to_addr = to_addr
        self.subject = subject
        self.message = message
        
    def show_message(self):
        return self.message
    
def main():
    name = " Joni "
    activity = "main game"
    message = f"Hallo {name}, jangan {activity} saja!"
    print(message)
    
    nama2 = {"Hendraman", "Sam", "Iman"}
    message2= f"{', '.join(nama2)}, mari kita kumpul."
    print(message2)
    
    # format string akses atribut & method dari objek
    email = Notification("darren@maranatha.ac.id", "robert@maranatha.ac.id", "Pesan rahasia...", "kita belajar format string di python")
    formatted = f"""
    From: <{email.from_addr}>
    To: <{email.to_addr}>
    Subject: {email.subject}>
    
    Hallo teman...
    {email.show_message()}
    Sampai jumpa....
    """
    print(formatted)
    
    # coba for
    format1 = f"{[2*a+1 for a in range(5)]}"
    print(format1)
    
    for n in range(1,8):
        print(f"{'kelipatan tiga' if n % 3 == 0 else n}")
        
    # format supaya rapi
    bil1 = 123
    bil2 = 456.7
    str1 = "string pendek"
    str2 = "string lebih panjang"
    format2 = f"{bil1}:7            ->[{bil1:7}]"
    format3 = f"{bil2}:7.2f       ->[{bil1:7.2f}]"
    format4 = f"{str1}:15s        ->[{str1:15s}]" #tambah spasi
    format5 = f"{str2}:15s        ->[{str2:15s}]" #tdk dipotong
    print(format2)
    print(format3)
    print(format4)
    print(format5)
    
    # nonstandard specifier
    tgl1 = datetime.datetime(2023, 12, 5 , 9, 30)
    format6 = f"Kuliah Paradigma Prg:{tgl1:%Y-%m-%d %I:M%p}"
    print(format6)
    
    # method format()
    from decimal import Decimal
    subtotal = Decimal('2.5') * Decimal('1.5')
    template = "{label}: {number:=^{size}.2f}"
    hasil1 = template.format(label="Amount", size=10, number=subtotal)
    print(hasil1)
    
    grand_total = subtotal * Decimal('12.11')
    hasil2 = template.format(label="Total", size=12, number = grand_total)
    print(hasil2)
    
if __name__ == "__main__":
    main()