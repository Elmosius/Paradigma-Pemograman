package P03e_Latihan_Percabangan_Pengulangan_Java_2272008_Elmosius_Suli;
// File : Switch_break.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket :

import java.util.*;
public class Switch_break {
    public static void main(String[] args) {
        int bil;
        Scanner sc = new Scanner(System.in);

        System.out.println("Masukkan sebuah bilangan : ");
        bil = sc.nextInt();

        switch(bil){
            case 0 :
                System.out.println(bil + " : bilangan nol");
                break;
            case 1 :
                System.out.println(bil + " : bilangan satu");
                break;
            case 2 :
                System.out.println(bil + " : bilangan dua");
                break;
            case 3 :
                System.out.println(bil + " : bilangan tiga");
                break;
            default :
                System.out.println(bil + " : bilangan lebih besar dari 3");
                break;
        }
        sc.close();
    }
}
