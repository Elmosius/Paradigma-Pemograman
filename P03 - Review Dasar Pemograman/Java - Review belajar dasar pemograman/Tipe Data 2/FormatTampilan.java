package P03c_Tugas_Tipe_Data_Java_2272008_Elmosius_Suli;
// File : SinCosTan2.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket :

import java.util.*;
import java.text.*;

public class FormatTampilan {
    public static void main(String[] args) {
        double bil;
        String nilaiOutput;
        Scanner sc = new Scanner(System.in);

        System.out.println("Masukkan suatu bilangan pecahan : ");
        bil = sc.nextDouble();

        System.out.println("Bilangan : \t\t     " + bil);

        NumberFormat formatAngka1 = NumberFormat.getNumberInstance();

        // format maksimal 5 digit desimal
        formatAngka1.setMaximumFractionDigits(5);
        nilaiOutput = formatAngka1.format(bil);

        System.out.print("Format max 5 digit desimal : ");
        System.out.println(nilaiOutput);

        // format maksimal 4 digit integer
        formatAngka1.setMaximumFractionDigits(4);
        nilaiOutput = formatAngka1.format(bil);

        System.out.print("Format max 4 digit desimal : ");
        System.out.println(nilaiOutput);

        NumberFormat formatAngka2 = NumberFormat.getNumberInstance();

        // format minimal 5 digit desimal
        formatAngka2.setMaximumFractionDigits(5);
        nilaiOutput = formatAngka2.format(bil);

        System.out.print("Format max 5 digit desimal : ");
        System.out.println(nilaiOutput);

        // format minimal 4 digit integer
        formatAngka2.setMaximumFractionDigits(4);
        nilaiOutput = formatAngka2.format(bil);

        System.out.print("Format max 4 digit desimal : ");
        System.out.println(nilaiOutput);
        sc.close();
    }
}
