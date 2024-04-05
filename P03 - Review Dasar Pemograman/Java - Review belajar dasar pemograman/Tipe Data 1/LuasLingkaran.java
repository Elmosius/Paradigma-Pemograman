package P03b_Latihan_Tipe_Data_Java_2272008_Elmosius_Suli;
// File : LuasLingkaran.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket :

import java.util.*;
public class LuasLingkaran {
    public static void main(String[] args) {
        double luas, keliling;
        int jari2;
        String nilaiOutput = "";
        Scanner sc = new Scanner(System.in);

        System.out.print("Masukkan jari-jari lingkaran : ");
        jari2 = sc.nextInt();
        
        luas = Math.PI * Math.pow(jari2, 2);
        keliling = 2 * Math.PI * jari2;

        nilaiOutput = "Jari2     = " + jari2 + "\n";
        nilaiOutput += "Luas     = " + luas + "\n";
        nilaiOutput += "Keliling = " + keliling;
        System.out.println(nilaiOutput);

        sc.close();
    }
}
