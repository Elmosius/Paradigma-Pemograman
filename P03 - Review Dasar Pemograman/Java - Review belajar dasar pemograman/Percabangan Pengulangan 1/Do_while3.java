package P03e_Latihan_Percabangan_Pengulangan_Java_2272008_Elmosius_Suli;
// File : Do_While3.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket :

import java.util.*;
public class Do_while3 {
    public static void main(String[] args) {
        int bil, c,diinginkan;
        Scanner sc = new Scanner(System.in);

        System.out.println("Tabel Penjumlahan & Perkalian s/d : ");
        bil = sc.nextInt();

        System.out.println("--> c   c+c     (c+c)   c*c");
        c= 1;
        do{
            System.out.print("--> " + c);
            System.out.print("\t" + c+c);  //mengapa hasilnya salah
             //Beberapa operator dalam Java memiliki prioritas yang berbeda. Jika operator-operator ini digunakan secara tidak tepat, maka akan menghasilkan hasil yang tidak diinginkan.
            System.out.print("\t" + (c+c));
            System.out.println("\t" + c*c);
            c++;
        } while (c <= bil);


    sc.close();
    }
}
