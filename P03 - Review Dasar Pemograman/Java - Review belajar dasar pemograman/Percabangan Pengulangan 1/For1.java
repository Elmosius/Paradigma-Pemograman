package P03e_Latihan_Percabangan_Pengulangan_Java_2272008_Elmosius_Suli;
// File : For1.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket :

import java.util.*;
public class For1 {
    public static void main(String[] args) {
        int bil, c;
        Scanner sc = new Scanner(System.in);

        System.out.println("Mengulang 1 s/d : ");
        bil = sc.nextInt();

        for(c =1; c<=bil; c++)
            System.out.println("--> " + c);

        sc.close();
    }
}
