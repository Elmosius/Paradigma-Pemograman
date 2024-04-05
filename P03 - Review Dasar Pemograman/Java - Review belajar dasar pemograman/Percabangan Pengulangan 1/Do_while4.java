package P03e_Latihan_Percabangan_Pengulangan_Java_2272008_Elmosius_Suli;
// File : Do_While3.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket :

import java.util.*;
public class Do_while4 {
    public static void main(String[] args) {
        int bil, c,d;
        Scanner sc = new Scanner(System.in);

        System.out.println("Tabel Perkalian s/d : ");
        bil = sc.nextInt();

        c= 1;
        do{
            d=1;
            do{
                System.out.print("\t" + c*d);
                d++;
            }while (d<=bil);
            System.out.println();
            c++;
        }while (c<=bil);
        

    sc.close();
    }
}
