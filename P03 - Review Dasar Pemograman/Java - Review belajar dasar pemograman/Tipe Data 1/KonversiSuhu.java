package P03b_Latihan_Tipe_Data_Java_2272008_Elmosius_Suli;

// File : KonversiSuhu.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket :

import java.util.*;
public class KonversiSuhu {
    public static void main(String[] args) {
        int celcius;
        Scanner sc = new Scanner(System.in);

        System.out.print("Suhu dalam celcius : ");
        celcius = sc.nextInt();

        double fahrenheit;

        fahrenheit = (double) 9 / (double) 5 * celcius + 32;
        System.out.println("Konversi suhu");
        System.out.println("Celcius     : " + celcius);
        System.out.println("Fahrenheit : " + fahrenheit);
    }
}
