# Exception: Membuat kelas exception sendiri
from decimal import Decimal

class InvalidWithDrawal(ValueError):
    def __init__(self, balance: Decimal, amount: Decimal) -> None:
        super().__init__(f"Saldo kurang dari ${amount}")
        self.amount = amount
        self.balance = balance
        
    def kelebihan(self) -> Decimal:
        return self.amount - self.balance
                       
def main():
    try:
        balance = Decimal('30.00')
        raise InvalidWithDrawal(balance, Decimal('50.00'))
    except InvalidWithDrawal as ex:
        print("Mohon maaf, jumlah penarikan anda melebihi "
              "saldo anda sebesar "
              f"${ex.kelebihan()}")
    
if __name__ == "__main__":
    main( )   