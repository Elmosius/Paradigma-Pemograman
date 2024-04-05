package P03c_Tugas_Tipe_Data_Java_2272008_Elmosius_Suli;
// File : PenjabaranDetik.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket : 

import java.util.*;
public class PenjabaranDetik {
    public static void main(String[] args) {
        int detik, hari, jam, menit;
        Scanner sc = new Scanner(System.in);

        final int satuHari = 60* 60 * 24;
        final int satuJam = 60 * 60;
        final int satuMenit = 60;

        System.out.print("Masukkan total detik yang akan dijabarkan : ");
        detik = sc.nextInt();

        System.out.println("Total waktu dalam detik : " + detik);

        hari = (int) (detik/satuHari);

        detik = detik - hari * satuHari;
        
        jam = (int) (detik/satuJam);

        detik -= jam * satuJam;

        menit = (int) (detik/satuMenit);

        detik -= menit * satuMenit;

        System.out.print("Penjabaran waktu : ");
        System.out.print(hari + " hari ");
        System.out.print(jam + " jam ");
        System.out.print(menit + " menit ");
        System.out.print(detik + " detik ");

        sc.close();
    }
}
