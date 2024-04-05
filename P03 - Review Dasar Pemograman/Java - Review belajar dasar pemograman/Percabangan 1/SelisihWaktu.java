package P03f_Tugas_Percabangan_Java_2272008_Elmosius_Suli;
// File : SelisihWaktu.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket : 

import java.util.*;
public class SelisihWaktu {
    public static void main(String[] args) {
        int jam1 = 0, menit1 = 0, detik1 = 0;
        int jam2 = 0, menit2 = 0, detik2 = 0;
        int jam = 0, menit = 0, detik = 0;

        Scanner sc = new Scanner(System.in);

        System.out.print("Jam awal      :");
        jam1 = sc.nextInt();
        System.out.print("Menit awal    :");
        menit1 = sc.nextInt();
        System.out.print("Detik awal    :");
        detik1 = sc.nextInt();

        System.out.print("Jam akhir     :");
        jam2 = sc.nextInt();
        System.out.print("Menit akhir   :");
        menit2 = sc.nextInt();
        System.out.print("Detik akhir   :");
        detik2 = sc.nextInt();

        detik1 = detik1 + (menit1*60) + (jam1 * 60 * 60);
        detik2 = detik2 + (menit2*60) + (jam2 *60 * 60);

        detik = detik1 - detik2;
        detik = Math.abs(detik);
        jam = (int) detik / (60 *60);
        detik = detik % (60*60);
        menit = (int) detik / 60;
        detik = detik % 60;

        System.out.println("Selisih: " + jam + " : " +
                            menit + " : " + detik);

        sc.close();
    }
}
