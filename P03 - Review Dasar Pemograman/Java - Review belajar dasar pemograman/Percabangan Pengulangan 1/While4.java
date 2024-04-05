package P03e_Latihan_Percabangan_Pengulangan_Java_2272008_Elmosius_Suli;
// File : While4.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket :

import java.util.*;
public class While4 {
    public static void main(String[] args) {
        int bil, c,d;
        Scanner sc = new Scanner(System.in);

        System.out.println("Tabel Perkalian s/d : ");
        bil = sc.nextInt();

        c= 1;
        while(c<=bil){
            d=1;
            while(d<=bil){
                System.out.print("\t" + c*d);
                d++;
            }
            System.out.println();
            c++;
        }
    sc.close();
    }
}
