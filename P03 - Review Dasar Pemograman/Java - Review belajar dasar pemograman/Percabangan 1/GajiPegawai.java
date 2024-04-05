package P03f_Tugas_Percabangan_Java_2272008_Elmosius_Suli;
// File : GajiPegawai.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket : 
import java.util.*;
public class GajiPegawai {
    public static void main(String[] args) {
        int gajiPokok, omset, targetOmset;
        double bonus;
        String kinerja;
        Scanner sc = new Scanner(System.in);

        System.out.print("Masukkan Gaji Pokok : ");
        gajiPokok = sc.nextInt();

        System.out.print("Masukkan omset : ");
        omset = sc.nextInt();

        System.out.print("Masukkan target omset : ");
        targetOmset = sc.nextInt();

        System.out.println("Gaji pokok : " + gajiPokok);
        System.out.println("Omset : " + omset);
        System.out.println("Target : " + targetOmset);

        if( omset >= (2* targetOmset)){
            bonus= 100 + 0.1 * (omset - targetOmset);
            kinerja = "Luar biasa";
        }
        else if (omset >= (1.5 * targetOmset)){
            bonus= 100 + 0.05 * (omset - targetOmset);
            kinerja = "Sangat baik";
        }
        else if (omset >= targetOmset){
            bonus= 100 + 0.025 * (omset - targetOmset);
            kinerja = "baik";
        }
        else{ //tidak memenuhi target omset
            bonus = 0;
            kinerja = "Anda dipecat";
        }
        System.out.println("Bonus       : " + bonus);
        System.out.println("Gaji Total  : " + (gajiPokok + bonus));
        System.out.println("Kinerja     : " + kinerja);

        sc.close();
    }
    



}
