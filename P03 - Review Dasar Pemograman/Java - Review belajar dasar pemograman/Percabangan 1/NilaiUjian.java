package P03f_Tugas_Percabangan_Java_2272008_Elmosius_Suli;
// File : NilaiUjian.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket : 

import java.util.*;
public class NilaiUjian {
    public static void main(String[] args) {
        int nilai;
        Scanner sc = new Scanner(System.in);

        System.out.print("Masukkan nilai ujian (dalam angka) : ");
        nilai = sc.nextInt();

        System.out.println("Nilai ujian: " + nilai);
        System.out.print("Anda mendapat ");

        if (nilai >= 80) {
            System.out.println("A");
        } else if (nilai >= 73) {
            System.out.println("B");
        } else if (nilai >= 55) {
            System.out.println("C");
        } else if (nilai >= 41) {
            System.out.println("D");
        } else {
            System.out.println("E");
        }


    }
}
