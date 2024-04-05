package P03e_Latihan_Percabangan_Pengulangan_Java_2272008_Elmosius_Suli;
// File : For3.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket :

import java.util.*;
public class For3 {
    public static void main(String[] args) {
        int bil, c, d;
        Scanner sc = new Scanner(System.in);

        System.out.println("Tabel Penjumlahan & Perkalian s/d");
        bil = sc.nextInt();

        System.out.println("--> c c+c (c+c) c*c");
        for (c = 1; c <= bil; c++) {
            System.out.print("--> " + c);
            System.out.print("  " + c+c);   //mengapa hasilnya salah? Kesalahan dalam penggunaan operator:
            //Beberapa operator dalam Java memiliki prioritas yang berbeda. Jika operator-operator ini digunakan secara tidak tepat, maka akan menghasilkan hasil yang tidak diinginkan.
            System.out.print("   " + (c+c));
            System.out.println("    " + c*c);
        }
    }
}
