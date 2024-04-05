package Praktikum.P04.P04c_Latihan_Inheritance_Java_227008_Elmosius_Suli;
// File : Pegawai.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket :
public class Pegawai {
    private String nama;
    private int gaji;

    // constructor
    public Pegawai(String namanya, int gajinya){
        this.nama = namanya;
        this.gaji = gajinya;

    }

    // method meminta nilai nama
    public String getNama(){
        return this.nama;
    }

    // method meminta nilai gaji
    public int getGaji(){
        return this.gaji;
    }
}
