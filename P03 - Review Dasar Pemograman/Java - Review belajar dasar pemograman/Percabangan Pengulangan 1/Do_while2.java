package P03e_Latihan_Percabangan_Pengulangan_Java_2272008_Elmosius_Suli;
// File : Do_While2.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket :

import java.util.*;
public class Do_while2 {
    public static void main(String[] args) {
        int bil, c;
        Scanner sc = new Scanner(System.in);

        System.out.println("Mengulang bil ganjil dari 1 s/d : ");
        bil = sc.nextInt();

        c= 1;
        do{
            System.out.println("--> " + c);
            c+=2;
        } while (c <= bil);


    sc.close();
    }
}
