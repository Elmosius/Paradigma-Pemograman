package P03b_Latihan_Tipe_Data_Java_2272008_Elmosius_Suli;

    // File : Boolean1.java
    // Nama : Elmosius Suli
    // NRP  : 2272008
    // Kelas : B
    // Ket : input dengan JOptionPane (bandingkan dg Boolean4)

import javax.swing.*;

public class Boolean1 {
    public static void main(String[] args) {
        int bil1, bil2;
        String nilaiInput;

        nilaiInput = JOptionPane.showInputDialog("Masukkan bilangan 1");
        bil1 = Integer.parseInt(nilaiInput);
        nilaiInput = JOptionPane.showInputDialog("Masukkan bilangan 2");
        bil2 = Integer.parseInt(nilaiInput);


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

    }
}
