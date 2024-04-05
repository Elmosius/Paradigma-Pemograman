package P03e_Latihan_Percabangan_Pengulangan_Java_2272008_Elmosius_Suli;
// File : For2.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket :

import java.util.*;
public class For2 {
    public static void main(String[] args) {
        int bil, c;
        Scanner sc = new Scanner(System.in);

        System.out.println("Mengulang bil ganjil dari 1 s/d : ");
        bil = sc.nextInt();

        for(c =1; c<=bil; c+=2)
            System.out.println("--> " + c);

        sc.close();
    }
}
