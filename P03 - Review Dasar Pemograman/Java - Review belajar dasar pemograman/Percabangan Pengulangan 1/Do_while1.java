package P03e_Latihan_Percabangan_Pengulangan_Java_2272008_Elmosius_Suli;
// File : Do_While1.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket :

import java.util.*;
public class Do_while1 {
    public static void main(String[] args) {
        int bil, c;
        Scanner sc = new Scanner(System.in);

        System.out.println("Mengilang 1 s/d : ");
        bil = sc.nextInt();

        c= 1;
        do{
            System.out.println("--> " + c);
            c++;
        } while (c <= bil);


    sc.close();
    }
}
