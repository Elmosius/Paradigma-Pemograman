package Praktikum.P05.P05b_Latihan_Polymorphism_Java_2272008_Elmosius_Suli;
// File : TestTypeCasting.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket : test type casting objek
public class TestPolymorphism {
    public static void main(String[] args) {
        Manusia m1 = new Manusia("Nyokap", 50, 165);
        Manusia m2 = new Mahasiswa("Sonia", 19, 170, "0472050", 'A');
        Manusia m3 = new Assisten("Chika", "0472017", "OOP Java", 10);

        Manusia m4 = new Mahasiswa("Eric", 20, 175, "0472035", 'B');
        Manusia m5 = new Assisten("Anto", "0472124", "Java lanjut", 8);

        System.out.println("Test Polymorphism");
        System.out.println("\nTipe Manusia,     Objek Manusia : " + m1.to_string() );
        System.out.println("\nTipe Manusia,     Objek Mahasiwa : " + m2.to_string() );
        System.out.println("\nTipe Manusia,     Objek Assisten : " + m3.to_string() );
        System.out.println("\nTipe Mahasiswa,   Objek Mahasiswa : " + m4.to_string() );
        System.out.println("\nTipe Mahasiswa,   Objek Assisten : " + m5.to_string() );
    }
}
