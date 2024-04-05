package P03c_Tugas_Tipe_Data_Java_2272008_Elmosius_Suli;
// File : SinCosTan1.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket : ( sudut dalam radian)
import java.util.*;
public class SinCosTan1 {
    public static void main(String[] args) {
        double sudut;
        double sinus, cosinus, tangen;
        Scanner sc = new Scanner(System.in);

        System.out.print("Masukkan besar sudut dalam radian (0.0 - 6.28)");
        sudut = sc.nextDouble();
        
        sinus = Math.sin(sudut);

        cosinus = Math.cos(sudut);

        tangen = Math.tan(sudut);

        System.out.println("Sudut: " + sudut + " rad");
        System.out.println("Sin("+sudut+"): " +sinus);
        System.out.println("Cos("+sudut+"): " +cosinus);
        System.out.println("Tan("+sudut+"): " +tangen);

        sc.close();
    }
}
