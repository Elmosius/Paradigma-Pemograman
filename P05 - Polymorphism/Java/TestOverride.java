package Praktikum.P05.P05b_Latihan_Polymorphism_Java_2272008_Elmosius_Suli;
// File : TestOverride.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket : test overriding method
public class TestOverride {
    public static void main(String[] args) {
        Manusia m1 = new Manusia("Nyokap", 50, 165);
        Mahasiswa m2 = new Mahasiswa("Sonia", 19, 170, "0472050", 'A');
        Assisten m3 = new Assisten("Chika", "0472017", "OOP Java", 10);

        System.out.println("Test Override");
        System.out.println("\nData orang tua : " + m1.to_string() );
        System.out.println("\nData mahasiswa : " + m2.to_string() );
        System.out.println("\nData asisten : " + m3.to_string() );
    }
}
