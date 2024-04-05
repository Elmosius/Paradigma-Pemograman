package P03e_Latihan_Percabangan_Pengulangan_Java_2272008_Elmosius_Suli;
// File : While1.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket :

import java.util.*;
public class While1 {
    public static void main(String[] args) {
        int bil, c;
        Scanner sc = new Scanner(System.in);

        System.out.println("Mengulang 1 s/d : ");
        bil = sc.nextInt();

        c= 1;
        while (c<=bil) {
            System.out.println("--> " + c);
            c++;
        }
    sc.close();
    }
}
