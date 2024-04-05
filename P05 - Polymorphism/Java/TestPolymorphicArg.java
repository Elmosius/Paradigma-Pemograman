package Praktikum.P05.P05b_Latihan_Polymorphism_Java_2272008_Elmosius_Suli;
// File : TestPolymorphicArg.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket : test polymorphic argument
public class TestPolymorphicArg {
    public static void main(String[] args) {
        Manusia m1 = new Manusia("Nyokap", 50, 165);
        Mahasiswa m2 = new Mahasiswa("Sonia", 19, 170, "0472050", 'A');
        Assisten m3 = new Assisten("Chika", "0472017", "OOP Java", 10);
        Penghasilan p = new Penghasilan();

        System.out.println("Test polymorphic Argument");
        System.out.println("\nPenghasilan orangtua, jenis : " + p.jenis(m1)
        + ", jumlah : " + p.jumlah(m1));
        System.out.println("\nPenghasilan mahasiswa, jenis : " + p.jenis(m2)
        + ", jumlah : " + p.jumlah(m2));
        System.out.println("\nPenghasilan asisten, jenis : " + p.jenis(m3)
        + ", jumlah : " + p.jumlah(m3));
    }
}
