package Praktikum.P05.P05b_Latihan_Polymorphism_Java_2272008_Elmosius_Suli;
// File : TestTypeCasing.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket : test type casting objek
public class TestTypeCasting {
    public static void main(String[] args) {
        Manusia m1 = new Manusia("Nyokap", 50, 165);
        Manusia m2 = new Mahasiswa("Sonia", 19, 170, "0472050", 'A');
        Manusia m3 = new Assisten("Chika", "0472017", "OOP Java", 10);
        Mahasiswa m4 = new Assisten("Anto", "0472124", "Java Lanjut", 8);
        
        System.out.println("Test Type Casting Objek");
        System.out.println("\nTipe Manusia,     Objek Manusia (m1) :");
        System.out.println("Hidden attr : tidak ada");
        System.out.println("\nTipe manusia,     Objek Mahasiswa (m2) :");
        System.out.println("Hidden attr : Nrp : " +((Mahasiswa)m2).nrp+ " Kelas : "
        + ((Mahasiswa)m2).kelas);
        System.out.println("\nTipe Manusia,     Objek Asisten (m3) : ");
        System.out.println("Hidden attr : Nrp : " +((Mahasiswa)m3).nrp+ " Kelas : "
        + ((Mahasiswa)m3).kelas + " Mk : " + ((Assisten)m3).matakuliah
        + " Jml jaga : " + ((Assisten)m3).jml_jaga);
        System.out.println("\nTipe Mahasiswa, Objek Assisten (m4) : ");
        System.out.println("Hidden attr : Mk  : " + ((Assisten)m4).matakuliah 
        + " Jml jaga : " + ((Assisten)m4).jml_jaga);

    }
}
