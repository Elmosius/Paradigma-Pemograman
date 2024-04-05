package P03g_Tugas_Pengulangan_Java_2272008_Elmosius_Suli;
// File : NilaiMean.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket : 
import java.util.*;
public class NilaiMean {
    public static void main(String[] args) {
        int bykNilai, nilai, totalNilai =0;
        double mean;

        Scanner sc = new Scanner(System.in);

        System.out.print("Tentukan banyak nilai : ");
        bykNilai = sc.nextInt();

        for(int i = 1; i <= bykNilai; i++){
            System.out.print("Masukkan nilai ke " + i + " : ");
            nilai = sc.nextInt();

            System.out.println("nilai " + i + " = " + nilai);

            totalNilai += nilai;
        }
        mean = totalNilai /bykNilai;

        System.out.println("Banyak nilai yang dihitung : " + bykNilai);
        System.out.println("Total jumlah nilai         : " + totalNilai);
        System.out.println("Rata-rata nilai            : " + mean);
        sc.close();
    }
}
