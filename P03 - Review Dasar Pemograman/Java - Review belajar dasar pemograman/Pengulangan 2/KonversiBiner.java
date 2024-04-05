package P03g_Tugas_Pengulangan_Java_2272008_Elmosius_Suli;
// File : KonversiBiner.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket : 
import java.util.*;
public class KonversiBiner {
    public static void main(String[] args) {
        int bil, sisa = 0;
        String bilBiner = "";
        Scanner sc = new Scanner(System.in);

        System.out.print("Masukkan suatu bilangan : ");
        bil = sc.nextInt();

        System.out.println("Bilangan desimal : " + bil);

        do{
            sisa = bil % 2;
            bil = (int)(bil / 2);
            bilBiner = sisa + bilBiner;
        } while(bil > 0);
        System.out.println("Bilangan biner : " + bilBiner);

        sc.close();
    }
}
