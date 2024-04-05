package Praktikum.P04.P04c_Latihan_Inheritance_Java_227008_Elmosius_Suli;
// File : TestHewanReptilUnggas.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket :
public class TestHewanReptilUnggas {
    public static void main(String[] args) {
        Hewan satwa = new Hewan();

        Reptil cicak = new Reptil();

        Unggas ayam = new Unggas();

        System.out.println("Yang menjadi ciri satwa:");
        satwa.bernafas();
        satwa.berkembangBiak();
        System.out.println();

        System.out.println("Yang menjadi ciri cicak:");
        cicak.bernafas();
        cicak.berkembangBiak();
        cicak.melata();
        System.out.println();
        
        System.out.println("Yang menjadi ciri ayam:");
        ayam.bernafas();
        ayam.berkembangBiak();
        ayam.berparuh();
        System.out.println();


    }
}
