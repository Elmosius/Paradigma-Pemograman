package Praktikum.P05.P05b_Latihan_Polymorphism_Java_2272008_Elmosius_Suli;
// File : TestKucing2an.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket : test homogeneous & hterogeneous array
public class TestHetero {
    public static void main(String[] args) {
        // test homogen
        Mahasiswa[] mhs = new Mahasiswa[3];
        mhs[0] = new Mahasiswa("Sonia", 19, 170, "0472050", 'A');
        mhs[1] = new Mahasiswa("Joky", 20, 165, "0472017", 'B');
        mhs[2] = new Mahasiswa("Christian", 18, 160, "0472021", 'A');

        System.out.println("Array dari objek yg Homogen : ");
        for(int c = 0; c < mhs.length; c++){
            System.out.println(mhs[c].to_string());
        }
        // test heterogen
        Manusia[] m = new Manusia[3];
        m[0] = new Manusia("Timo", 23, 170);
        m[1] = new Mahasiswa("Ricky", 20, 165, "0472017", 'B');
        m[2] = new Assisten("Christian", "0472124", "OOP Java", '8');

        System.out.println("\nArray dari objek yg Heterogen");
        for(int c = 0; c<m.length; c++){
            System.out.println(m[c].to_string());        

        }
    }
}