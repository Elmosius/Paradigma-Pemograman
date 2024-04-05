package Praktikum.P04.P04c_Latihan_Inheritance_Java_227008_Elmosius_Suli;
// File : Mobil.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket :
public class Mobil extends Kendaraan{
    public String bahanBakar;
    public String mesin;

    // constructor
    public Mobil(){
        this.bahanBakar = "Bensin";
        this.mesin = "EFI";
        super.kecepatanMaks = 100;
        super.kapasitasPenumpang = 4;
    }
}
