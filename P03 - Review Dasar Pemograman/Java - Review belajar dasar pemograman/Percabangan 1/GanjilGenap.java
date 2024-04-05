package P03f_Tugas_Percabangan_Java_2272008_Elmosius_Suli;
// File : GanjilGenap.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket : 

import java.util.*;
public class GanjilGenap {
    public static void main(String[] args) {
        int bil;
        Scanner sc = new Scanner(System.in);

        System.out.print("Masukkan suatu bilangan : " );
        bil = sc.nextInt();

        if (bil % 2 == 0) {
            System.out.println(bil + " adalah bilangan genap");
        } else {
            System.out.println(bil + " adalah bilangan ganjil");
        }


        /*atau bisa juga ditulis seperti ini:
        if (bil % 2 != 0) {
            System.out.println(bil + " adalah bilangan ganjil");
        } else {
            System.out.println(bil + " adalah bilangan genap");
        }
         */
        sc.close();
    }
}
