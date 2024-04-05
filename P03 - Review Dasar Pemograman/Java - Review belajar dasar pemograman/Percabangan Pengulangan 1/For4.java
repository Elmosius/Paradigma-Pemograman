package P03e_Latihan_Percabangan_Pengulangan_Java_2272008_Elmosius_Suli;
// File : For4.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket :

import java.util.*;
public class For4 {
    public static void main(String[] args) {
        int bil, c, d;
        Scanner sc = new Scanner(System.in);

        System.out.println("Tabel Perkalian s/d");
        bil = sc.nextInt();

        for (c = 1; c <= bil; c++) {
            for (d = 1; d <= bil; d++) {
                System.out.print("\t" + c*d);
            }
            System.out.println();
        }
    }
}
