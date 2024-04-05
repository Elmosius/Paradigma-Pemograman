package P03c_Tugas_Tipe_Data_Java_2272008_Elmosius_Suli;

import java.util.Scanner;

// File : SinCosTan2.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket : (sudut dalam derajat)
public class SinCosTan2 {
    public static void main(String[] args) {
        double sudut;
        double sinus, cosinus, tangen, sudut_rad, pi;
        Scanner sc = new Scanner(System.in);

        System.out.print("Masukkan besar sudut dalam derajat : ");
        sudut = sc.nextInt();
        
        pi = 4.0 * Math.atan(1); //pi paling akurat

        //konversi sudut ke radian
        // PI radian = 180 derajat
        // t terajat = PI /  180 * t radian

        sudut_rad = pi / 180.0 * sudut;

        sinus = Math.sin(sudut_rad);
        cosinus = Math.cos(sudut);
        tangen = Math.tan(sudut);

        System.out.println("Sudut: " + sudut + " rad");
        System.out.println("Sin("+sudut+"): " +sinus);
        System.out.println("Cos("+sudut+"): " +cosinus);
        System.out.println("Tan("+sudut+"): " +tangen);

        sc.close();
    }
}
