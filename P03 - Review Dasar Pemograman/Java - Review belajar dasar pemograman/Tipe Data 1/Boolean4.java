package P03b_Latihan_Tipe_Data_Java_2272008_Elmosius_Suli;
  // File : Boolean4.java
    // Nama : Elmosius Suli
    // NRP  : 2272008
    // Kelas : B
    // Ket : test boolean dengan memangiil kelas ConsoleIn

    import java.io.*;
    import java.util.*;

public class Boolean4 {
    public static void main(String[] args) {
        int bil1, bil2;
        Scanner sc = new Scanner(System.in);

        System.out.print("Masukkan bilangan 1 : ");
        bil1 = sc.nextInt();
    
        System.out.print("Masukkan bilangan 2 : ");
        bil2 = sc.nextInt();

        boolean kondisi;

        kondisi = (bil1 == bil2);
        System.out.println(bil1 + " == " + bil2 + "\t: " + kondisi);

        
        kondisi = (bil1 != bil2);
        System.out.println(bil1 + " != " + bil2 + "\t: " + kondisi);

        
        kondisi = (bil1 > bil2);
        System.out.println(bil1 + " > " + bil2 + "\t: " + kondisi);

        
        kondisi = (bil1 >= bil2);
        System.out.println(bil1 + " >= " + bil2 + "\t: " + kondisi);

        kondisi = (bil1 < bil2);
        System.out.println(bil1 + " < " + bil2 + "\t: " + kondisi);

        
        kondisi = (bil1 <= bil2);
        System.out.println(bil1 + " <= " + bil2 + "\t: " + kondisi);

        sc.close();
    }
}
