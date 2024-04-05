package P03e_Latihan_Percabangan_Pengulangan_Java_2272008_Elmosius_Suli;
// File : Simple_if_else.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket :

import java.util.*;
public class Simple_if_else {
    public static void main(String[] args) {
        int bil;
        Scanner sc = new Scanner(System.in);

        System.out.println("Masukkan sebuah bilangan : ");
        bil = sc.nextInt();

        if(bil % 2 == 0)
            System.out.println(bil + " : bilangan genap");
        else
            System.out.println(bil + " : bilangan ganjil");
        
        sc.close();
    }   
}
