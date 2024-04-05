package Praktikum.P04.P04c_Latihan_Inheritance_Java_227008_Elmosius_Suli;
// File : Kereta.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket :
public class Kereta extends Kendaraan {
    public String tenagaPenarik;
    public int jmlPenarik;

    // constructor
    public Kereta(){
        this.tenagaPenarik = "Kuda";
        this.jmlPenarik = 2;
        super.kecepatanMaks = 50;
        super.kapasitasPenumpang = 8;
    }
}
