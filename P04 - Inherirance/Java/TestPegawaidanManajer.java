package Praktikum.P04.P04c_Latihan_Inheritance_Java_227008_Elmosius_Suli;
// File : TestPegawaidanManajer.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket :
public class TestPegawaidanManajer {
    public static void main(String[] args) {
        Manajer boss = new Manajer("Unyil", 25000);

        Pegawai staff1 = new Pegawai("Cuplis", 20000);

        Pegawai staff2 = new Pegawai("Pak Ogah", 100);

        boss.setBonus(500);

        System.out.println("Data Pegawai:");
        System.out.println("Boss:");
        System.out.println("\tNama : " + boss.getNama());
        System.out.println("\tGaji : " + boss.getGaji());

        System.out.println("\nStaff 1:");
        System.out.println("\tNama : " + staff1.getNama());
        System.out.println("\tGaji : " + staff1.getGaji());

        System.out.println("\nStaff 2:");
        System.out.println("\tNama : " + staff2.getNama());
        System.out.println("\tGaji : " + staff2.getGaji());
    }
}
