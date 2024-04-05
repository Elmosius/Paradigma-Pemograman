package P03e_Latihan_Percabangan_Pengulangan_Java_2272008_Elmosius_Suli;
// File : If_else_if.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket :

import java.util.*;
public class If_else_if {
    public static void main(String[] args) {
        int bil;
        Scanner sc = new Scanner(System.in);

        System.out.println("Masukkan sebuah bilangan : ");
        bil = sc.nextInt();
        
        if(bil > 0)
            System.out.println(bil + " : bilangan positif");
        else if (bil < 0)
            System.out.println(bil + " : bilangan negatif");
        else
            System.out.println(bil + " : bilangan nol");

        sc.close();
    }   
}
