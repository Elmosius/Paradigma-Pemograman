package P03f_Tugas_Percabangan_Java_2272008_Elmosius_Suli;
// File : TahunKabisat.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket : 

import java.util.*;
public class TahunKabisat {
    public static void main(String[] args) {
        int tahun;
        Scanner sc = new Scanner(System.in);

        System.out.print("Masukkan tahun : ");
        tahun = sc.nextInt();

        System.out.println("Tahun " + tahun);

        if (tahun % 4 == 0) {
            System.out.println("Bukan Tahun Kabisat");
        }else if((tahun % 100 == 0) && (tahun % 400 != 0)){
            System.out.println("Bukan Tahun Kabisat");
        }else{
            System.out.println("Tahun Kabisat");
        }
        sc.close();
    }
}
