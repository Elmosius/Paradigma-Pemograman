package Praktikum.P04.P04c_Latihan_Inheritance_Java_227008_Elmosius_Suli;
// File : TestMobildanKereta.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket :
public class TestMobildanKereta {
    public static void main(String[] args) {
        Mobil sedan = new Mobil();

        System.out.println("Sedanku:");
        System.out.println("Kecepatan Maks: " + sedan.kecepatanMaks);
        System.out.println("Kapasitas Penumpang: " + sedan.kapasitasPenumpang);
        System.out.println("Bahan Bakar: " + sedan.bahanBakar);
        System.out.println("Jenis Mesin: " + sedan.mesin);

        Kereta andong = new Kereta();
        System.out.println("\nAndongku:");
        System.out.println("Kecepatan Maks: " + andong.kecepatanMaks);
        System.out.println("Kapasitas Penumpang: " + andong.kapasitasPenumpang);
        System.out.println("Tenaga Penarik: " + andong.tenagaPenarik);
        System.out.println("Jumlah Penarik: " + andong.jmlPenarik);


    }
}
