package P03g_Tugas_Pengulangan_Java_2272008_Elmosius_Suli;
// File : KarakterSusun.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket : 
import java.util.*;
public class KarakterSusun {
    public static void main(String[] args) {
        int jmlSusun;
        String karakter;
        Scanner sc = new Scanner(System.in);
    
        System.out.print("Masukkan karakter yang akan disusun : ");
        karakter = sc.next();

        System.out.print("Tentukan tingkat susunan : ");
        jmlSusun = sc.nextInt();

        for(int i=0; i<jmlSusun; i++){
            for(int j=0; j<1; j++){
                System.out.print(karakter); 
            }
            System.out.println();
        }
        sc.close();
    }
}
