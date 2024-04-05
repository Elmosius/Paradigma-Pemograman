package P03f_Tugas_Percabangan_Java_2272008_Elmosius_Suli;
// File : SudutJam.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket : 

import java.util.*;
public class SudutJam {
    public static void main(String[] args) {
        int jam = 0;
        int menit = 0;
        double sudutJam, sudutMenit, sudut;
        Scanner sc =  new Scanner(System.in);

        System.out.print("Masukkan jam : ");
        jam = sc.nextInt();

        System.out.print("Masukkan menit : ");
        menit = sc.nextInt();

        sudutMenit = menit * 6;
        sudutJam = jam *30 + menit * 0.5;
        sudut = Math.abs(sudutJam - sudutMenit);

        if(sudut >180){
            sudut = 360 - sudut;
        }

        System.out.println("Sudut terkecil yang terbentuk: " + sudut);
        sc.close();
    }
}
