package P03g_Tugas_Pengulangan_Java_2272008_Elmosius_Suli;
// File : PrediksiTabungan.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket : 
import java.util.*;
public class PrediksiTabungan {
    public static void main(String[] args) {
        int targetTabungan, tabunganBulanan;
        int bulan = 0, tahun = 0;
        double bunga, totalTabungan = 0;
        Scanner sc = new Scanner(System.in);

        System.out.print("Target tabungan yang diinginkan : ");
        targetTabungan = sc.nextInt();

        System.out.print("Jumlah dana yang ditabung per bulan : ");
        tabunganBulanan = sc.nextInt();

        System.out.print("Bunga bank dalam % : ");
        bunga = sc.nextDouble();

        while(totalTabungan < targetTabungan){
            totalTabungan += tabunganBulanan;
            totalTabungan += totalTabungan * bunga /100;
            bulan++;
        }

        tahun = (int)(bulan / 12);
        bulan -= tahun*12;

        System.out.println("Target Tabungan     :"+targetTabungan);
        System.out.println("Tabungan Per Bulan  :"+tabunganBulanan);
        System.out.println("Bunga Bank          :"+ bunga + "%");
        System.out.println("Target akan terpenuhi " + "setelah menabung selama");
        System.out.println(tahun +" tahun," + bulan + " bulan");
        System.out.println("dengan total tabungan " + totalTabungan);
        sc.close();

    }
}
