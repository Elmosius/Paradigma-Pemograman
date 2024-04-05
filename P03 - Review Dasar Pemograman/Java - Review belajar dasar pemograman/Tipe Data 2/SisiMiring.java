package P03c_Tugas_Tipe_Data_Java_2272008_Elmosius_Suli;

import java.util.Scanner;

// File : SisiMiring.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket : 
public class SisiMiring {
    public static void main(String[] args) {
        int a,b;
        Scanner sc = new Scanner(System.in);

        System.out.println("Mencari panjang sisi miring segitiga siku-siku");
        System.out.print("Panjang sisi vertikal");
        a = sc.nextInt();

        System.out.print("Panjang sisi horizontal : ");
        b = sc.nextInt();

        double c;
        c = Math.sqrt(Math.pow(a,2) + Math.pow(b,2));

        System.out.println("Rumus Phytagpras");
        System.out.println("Sisi vertikal     : " + a);
        System.out.println("Sisi horizontal :" + b);
        System.out.println("Sisi Miring     : " + c);

        sc.close();
    }
}
