package Praktikum.P04.P04c_Latihan_Inheritance_Java_227008_Elmosius_Suli;
// File : Manajer.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket :
public class Manajer extends Pegawai{
    private int bonus;

    // constructor
    public Manajer(String namanya, int gajinya){
        super(namanya, gajinya);
    }

    // method memberi nilai bonus
    public void setBonus(int bonusnya){
        this.bonus = bonusnya;
    }

    // method meminta nilai gaji
    public int getGaji(){
        int gajiPokok = super.getGaji();
        return gajiPokok + this.bonus;
    }
}
