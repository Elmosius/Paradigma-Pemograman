package Praktikum.P04.P04c_Latihan_Inheritance_Java_227008_Elmosius_Suli;
// File : Kendaraan.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket :
public class Kendaraan {
    protected int kecepatanMaks;
    protected int kapasitasPenumpang;
    private static int jmlKendaraan = 0;

    // constructor
    public Kendaraan(){
        this.kecepatanMaks = 0;
        this.kapasitasPenumpang = 0;
        this.jmlKendaraan++;
    }
}
