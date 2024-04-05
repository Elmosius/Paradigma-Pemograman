package P03e_Latihan_Percabangan_Pengulangan_Java_2272008_Elmosius_Suli;
// File : Switch_nobreak.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket :

import java.util.*;
public class Switch_nobreak {
    public static void main(String[] args) {
        int bil;
        Scanner sc = new Scanner(System.in);

        System.out.println("Masukkan sebuah bilangan antara 1 s/d 5: ");
        bil = sc.nextInt();

        switch(bil){
            case 1 :
                System.out.println(bil + " : bilangan <= 1");
            case 2 :
                System.out.println(bil + " : bilangan <= 2");
            case 3 :
                System.out.println(bil + " : bilangan <= 3");
            case 4 :
                System.out.println(bil + " : bilangan <= 4");
            case 5 :
                System.out.println(bil + " : bilangan <= 5");
                break;
            default :
                System.out.println("Kalo baca petunjuk yg bener dong !");
            }       
        sc.close();
    }
}
