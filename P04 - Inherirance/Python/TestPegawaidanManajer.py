# File TestPegawaidanManajer
from Manajer import Manajer
from Pegawai import Pegawai

def main():
    boss = Manajer("Unyil", 25000)
    staff1 = Pegawai("Cuplis", 20000)
    staff2 = Pegawai("Pak Ogah", 100)
    boss.bonus = 500
    
    print("Data Pegawai:")
    print("Boss:")
    print("\tNama : " + boss.nama)
    print("\tGaji : " + str(boss.gaji))
    
    print("\nStaff 1:")
    print("\tNama : " + staff1.nama)
    print("\tGaji : " + str(staff1.gaji))
    
    
    print("\nData Pegawai:")
    print("\tNama : " + staff2.nama)
    print("\tGaji : " + str(staff2.gaji))
    
if __name__ == "__main__":
    main()