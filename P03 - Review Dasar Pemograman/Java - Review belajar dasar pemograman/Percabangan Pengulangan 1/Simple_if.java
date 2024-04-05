package P03e_Latihan_Percabangan_Pengulangan_Java_2272008_Elmosius_Suli;
// File : Simple_if.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket :

import java.util.*;
public class Simple_if {
    public static void main(String[] args) {
        int bil;
        Scanner sc = new Scanner(System.in);

        System.out.println("Masukkan sebuah bilangan : ");
        bil = sc.nextInt();

        if(bil >= 10);      //if tanpa block
        System.out.println("Bilangan lebih besar dari 10");
    
        if(bil == 0 ){      //if dengan block
            System.out.println("Bilangan sama dengan 0");
            System.out.println("Hati-hati jangan membagi dengan bilangan ini !");
        }
    sc.close();    
    }   
}
